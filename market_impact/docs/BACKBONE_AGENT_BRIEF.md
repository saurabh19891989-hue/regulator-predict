# BACKBONE_AGENT_BRIEF.md — driver-to-driver transmission graph (binding)

You build part of the macro/commodity "backbone" of the Market Impact Graph (repo `/home/user/regulator-predict`):
directed, signed, weighted edges BETWEEN DRIVER NODES (FACTOR, POLICY, COUNTRY, THEME) — how a shock to one driver
moves another. These edges create the 2nd/3rd/4th-order effects (e.g. `C_MIDEAST_CONFLICT` → `F_BRENT` →
`F_USDINR` → `F_CPI_IN` → `F_REPO_IN` → `F_HOUSING_DEMAND`).
Read first: `market_impact/PLAN.md`, `market_impact/docs/AGENT_SPEC.md` (§2 units, §3 edge object — binding),
`market_impact/graph/nodes_seed.json`, `market_impact/results/factor_state.md`.

Rules:
- Weight `w` = change in the target in TARGET SSU per +1 SOURCE SSU (both SSUs are defined in nodes_seed.json).
  Example: Brent +10% (1 SSU) → India CPI +0.3 pp ⇒ target SSU is +1 pp ⇒ w = +0.3. Show the arithmetic in `mechanism`.
- Ground weights in published elasticities where possible (RBI Monetary Policy Reports, IMF/BIS/World Bank studies,
  ministry data) and cite them; otherwise mark `"source": "model knowledge"` with lower confidence.
- Only material, direct transmissions (one causal step). Do not add an edge A→C if it is fully explained by A→B→C.
- Include feedback/policy-reaction edges (e.g. `F_CPI_IN` → `F_REPO_IN`, `F_USDINR` → `F_FPI_FLOWS`, `F_STEEL_INDIA` →
  `P_STEEL_DUTY_IN` reversed sign where policy reacts), but avoid tight 2-node cycles with |w| products ≥ 1.
- Target 120–180 edges for your part. Propose missing drivers in `new_nodes_proposed` (id `NEW_*`, type, name, ssu).

Write `market_impact/graph/backbone_<PART>.json` = `{"edges": [...], "new_nodes_proposed": [...], "notes": "..."}`,
run `python3 -m market_impact.mi.check market_impact/graph/backbone_<PART>.json`, fix all errors. Do not run git.
Final reply ≤100 words.
