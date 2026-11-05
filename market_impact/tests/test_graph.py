import math

from market_impact.mi.graph import DAMP, Network


def test_multi_order_propagation_and_sinks():
    nodes = {"EV": {"type": "FACTOR"}, "F1": {"type": "FACTOR"}, "F2": {"type": "FACTOR"},
             "A": {"type": "COMPANY"}, "B": {"type": "COMPANY"}, "C": {"type": "COMPANY"}}
    E = lambda s, d, w, layer="backbone": {"src": s, "dst": d, "w": w, "w_low": w, "w_high": w, "layer": layer}
    edges = [E("F1", "F2", 0.5), E("F2", "F1", 0.4),            # cycle must not loop
             E("F1", "A", 10, "company"), E("F2", "B", -6, "company"),
             E("A", "C", 0.3, "company_link"),                  # allowed company link
             E("B", "C", 9.0, "company")]                       # company→company non-link: must NOT propagate
    net = Network(nodes, edges)
    tot, by_order, paths = net.unit_response("F1")
    assert math.isclose(tot["A"], 10 * DAMP[1])                             # 1st order
    assert math.isclose(tot["B"], 0.5 * -6 * DAMP[2])                       # 2nd order via F2
    assert "C" not in tot                                                   # driver shocks stop at companies
    tC, _, _ = net.unit_response("A")                                       # idiosyncratic shock at A
    assert math.isclose(tC["C"], 0.3 * DAMP[1])                             # spills over via the company link
    assert set(by_order["B"]) == {2} and set(by_order["A"]) == {1}
    assert all(len(p) <= 4 for p, _, _ in paths)
    # 4th-order chain
    nodes4 = {k: {"type": "FACTOR"} for k in ("S", "X", "Y", "Z")}
    nodes4["Q"] = {"type": "COMPANY"}
    e4 = [E("S", "X", 2), E("X", "Y", 2), E("Y", "Z", 2), E("Z", "Q", 2, "company")]
    t4, o4, _ = Network(nodes4, e4).unit_response("S")
    assert math.isclose(t4["Q"], 16 * DAMP[4]) and set(o4["Q"]) == {4}


def test_clamped_observed_driver_blocks_upstream_propagation():
    nodes = {"BRENT": {"type": "FACTOR"}, "INR": {"type": "FACTOR"}, "X": {"type": "COMPANY"}}
    E = lambda s, d, w, layer="backbone": {"src": s, "dst": d, "w": w, "w_low": w, "w_high": w, "layer": layer}
    net = Network(nodes, [E("BRENT", "INR", 0.4), E("INR", "X", 5, "company"), E("BRENT", "X", -2, "company")])
    free, _, _ = net.unit_response("BRENT")
    clamped, _, _ = net.unit_response("BRENT", clamped=frozenset({"INR"}))
    assert math.isclose(free["X"], -2 + 0.4 * 5 * DAMP[2])
    assert math.isclose(clamped["X"], -2)          # INR observed separately → no double count via BRENT→INR
