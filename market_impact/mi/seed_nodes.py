"""Seed node vocabulary for the Exposure Propagation Network.

Run: python3 -m market_impact.mi.seed_nodes  → market_impact/graph/nodes_seed.json
SSU = standard shock unit: the size of a "+1" move of the node. Edge weights are in target SSU per +1 source SSU;
company targets are in % equity value.
"""
import csv
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (id, name, SSU definition, yahoo series or None)
FACTORS = [
    # energy
    ("F_BRENT", "Brent crude oil price", "+10% Brent", "BZ=F"),
    ("F_GAS_GLOBAL", "Global natural gas / LNG price", "+15% gas/LNG price", "NG=F"),
    ("F_COAL_INTL", "International thermal coal price", "+15% seaborne thermal coal", "MTF=F"),
    ("F_COAL_INDIA", "Indian domestic coal price & availability cost", "+10% domestic coal cost (notified/e-auction)", None),
    ("F_COKING_COAL", "Coking coal price", "+15% coking coal", None),
    ("F_POWER_PRICE_IN", "Indian power exchange (IEX) prices", "+15% average spot power price", None),
    ("F_POWER_DEMAND_IN", "Indian electricity demand", "+3 pp demand growth", None),
    ("F_REFINING_MARGIN", "Refining margins (GRM / cracks)", "+$2/bbl gross refining margin", "HO=F"),
    ("F_PETROCHEM_SPREADS", "Petrochemical / polymer spreads", "+10% polymer-naphtha spreads", None),
    # metals
    ("F_STEEL_GLOBAL", "Global HRC steel price", "+10% global HRC", "HRC=F"),
    ("F_STEEL_INDIA", "Indian domestic steel price", "+7% domestic HRC/rebar price", None),
    ("F_IRON_ORE", "Iron ore price", "+15% iron ore", "TIO=F"),
    ("F_COPPER", "Copper price", "+10% copper", "HG=F"),
    ("F_ALUMINIUM", "Aluminium price", "+10% aluminium", "ALI=F"),
    ("F_ZINC_LEAD", "Zinc / lead price", "+10% zinc", None),
    ("F_GOLD", "Gold price", "+8% gold (USD)", "GC=F"),
    ("F_SILVER", "Silver price", "+12% silver", "SI=F"),
    ("F_BATTERY_MATERIALS", "Lithium / battery cell cost", "+15% battery cell cost", None),
    # agri & soft commodities
    ("F_WHEAT", "Wheat price", "+10% wheat", "ZW=F"),
    ("F_RICE", "Rice price", "+10% rice", None),
    ("F_SUGAR", "Sugar price", "+10% sugar", "SB=F"),
    ("F_COTTON", "Cotton price", "+10% cotton", "CT=F"),
    ("F_EDIBLE_OIL", "Palm / edible oil price", "+10% edible oils", "ZS=F"),
    ("F_DAIRY", "Milk / dairy input cost", "+8% milk procurement price", None),
    ("F_COCOA_COFFEE_TEA", "Cocoa, coffee, tea prices", "+15% beverage commodities", None),
    ("F_PACKAGING", "Packaging cost (paper, plastics)", "+10% packaging cost", None),
    ("F_FERTILISER_INPUTS", "Ammonia / urea / phosphate input prices", "+15% fertiliser inputs", None),
    ("F_CHEM_FEEDSTOCK", "Chemical feedstock (benzene, propylene, etc.)", "+10% feedstock", None),
    ("F_RUBBER", "Natural / synthetic rubber price", "+10% rubber", None),
    # FX
    ("F_USDINR", "USD/INR exchange rate", "+3% USD/INR (rupee weaker)", "INR=X"),
    ("F_DXY", "US dollar index", "+3% DXY", "DX-Y.NYB"),
    ("F_USDCNY", "USD/CNY", "+3% USD/CNY (yuan weaker)", "CNY=X"),
    # rates, liquidity, flows
    ("F_REPO_IN", "RBI repo rate", "+25 bp repo", None),
    ("F_GSEC_10Y_IN", "India 10-year G-sec yield", "+25 bp yield", None),
    ("F_LIQUIDITY_IN", "Indian banking system liquidity", "+1 lakh crore surplus liquidity", None),
    ("F_CREDIT_SPREADS_IN", "Indian corporate credit spreads", "+50 bp spreads", None),
    ("F_US_10Y", "US 10-year Treasury yield", "+25 bp yield", "^TNX"),
    ("F_FED_FUNDS", "US Fed funds rate", "+25 bp", "^IRX"),
    ("F_FPI_FLOWS", "Foreign portfolio flows into Indian equities", "+US$5 bn net inflow per quarter", None),
    ("F_DOMESTIC_FLOWS", "Domestic SIP / DII flows", "+10% monthly SIP + DII inflow", None),
    ("F_EQUITY_ACTIVITY_IN", "Indian equity market volumes & retail activity", "+20% traded value / demat additions", None),
    ("F_RISK_SENTIMENT", "Global risk aversion (VIX)", "+5 VIX points", "^VIX"),
    ("F_US_EQUITIES", "US equity market", "+5% S&P 500", "^GSPC"),
    # Indian macro
    ("F_GDP_IN", "India real GDP growth", "+1 pp", None),
    ("F_CPI_IN", "India CPI inflation", "+1 pp", None),
    ("F_FOOD_INFLATION_IN", "India food inflation", "+2 pp", None),
    ("F_RURAL_DEMAND", "Rural consumption growth", "+5 pp", None),
    ("F_URBAN_DEMAND", "Urban discretionary consumption growth", "+5 pp", None),
    ("F_MONSOON", "Monsoon rainfall vs normal", "+10% above long-period average", None),
    ("F_GOVT_CAPEX", "Central + state government capex", "+10% capex growth", None),
    ("F_PRIVATE_CAPEX", "Private corporate capex", "+10% capex growth", None),
    ("F_HOUSING_DEMAND", "Residential real-estate sales", "+10% sales volume", None),
    ("F_CREDIT_GROWTH_IN", "Bank credit growth", "+3 pp", None),
    ("F_DEPOSIT_GROWTH_IN", "Bank deposit growth / funding ease", "+3 pp", None),
    ("F_ASSET_QUALITY_IN", "Credit cost / NPA cycle (higher = worse)", "+50 bp credit cost", None),
    ("F_UNSECURED_STRESS", "Unsecured retail & microfinance stress (higher = worse)", "+1 pp delinquencies", None),
    ("F_WAGES_IN", "Indian wage / employee-cost inflation", "+2 pp", None),
    ("F_TRAVEL_DEMAND", "Air/hotel/tourism demand", "+10%", None),
    ("F_GOLD_DEMAND_IN", "Indian jewellery/gold demand volume", "+10%", None),
    ("F_AUTO_DEMAND_IN", "Indian vehicle demand", "+10% volumes", None),
    # global macro
    ("F_US_GDP", "US growth", "+1 pp", None),
    ("F_EU_GDP", "Europe growth", "+1 pp", None),
    ("F_CHINA_GDP", "China growth / stimulus", "+1 pp", None),
    ("F_CHINA_STEEL_EXPORTS", "China steel exports", "+15% y/y", None),
    ("F_CHINA_CHEM_EXPORTS", "China chemical/API dumping intensity", "+15% export volumes / price cuts", None),
    ("F_US_TECH_SPEND", "US/EU enterprise IT services spend", "+5% growth", None),
    ("F_AI_CAPEX", "Global AI / data-centre capex", "+10% growth", None),
    ("F_US_GENERIC_PRICING", "US generic drug price erosion (higher = worse)", "+5 pp erosion", None),
    ("F_SHIPPING_RATES", "Global container / freight rates", "+25%", None),
    ("F_GULF_REMITTANCES", "Gulf economy / remittances", "+10%", None),
    ("F_SEMICONDUCTOR_SUPPLY", "Chip/electronics component supply tightness (higher = tighter)", "+1 = tightening", None),
]

POLICIES = [
    ("P_US_TARIFF_INDIA", "US tariffs on Indian goods", "+10 pp average tariff"),
    ("P_US_PHARMA_TARIFF", "US tariffs on pharmaceuticals", "+10 pp on Indian pharma exports"),
    ("P_US_VISA_OUTSOURCING", "US H-1B / outsourcing restrictions", "+1 = material tightening"),
    ("P_STEEL_DUTY_IN", "Indian safeguard/anti-dumping duty on steel imports", "+10 pp effective duty"),
    ("P_ANTI_DUMPING_IN", "Indian anti-dumping duties (chemicals, solar, others)", "+1 = new broad duties"),
    ("P_GST_CONSUMPTION", "GST rate cuts on consumer goods/services", "+1 = broad cut (~2-5 pp on affected items)"),
    ("P_FUEL_TAX_IN", "Fuel excise / retail price policy (+ = higher taxes/regulated squeeze)", "+1 = Rs 2/litre excise rise"),
    ("P_WINDFALL_EXPORT_TAX", "Windfall / export taxes on commodities", "+1 = imposition"),
    ("P_PLI", "Production-linked incentive schemes", "+1 = expansion/disbursement"),
    ("P_DEFENCE_PROCUREMENT", "Indian defence procurement & indigenisation", "+10% domestic orders"),
    ("P_RAILWAY_CAPEX", "Railway capex", "+10%"),
    ("P_RENEWABLE_SUPPORT", "Renewable / transmission policy support", "+1 = stronger support"),
    ("P_EV_POLICY", "EV incentives / mandates", "+1 = stronger EV push"),
    ("P_SEBI_DERIVATIVES", "SEBI F&O / market-structure tightening", "+1 = tightening step"),
    ("P_RBI_PRUDENTIAL", "RBI prudential tightening (risk weights, LCR, provisioning)", "+1 = tightening step"),
    ("P_TELECOM_TARIFFS", "Mobile tariff hikes", "+10% ARPU via tariff hike"),
    ("P_USFDA_ENFORCEMENT", "USFDA inspection/enforcement intensity", "+1 = stricter"),
    ("P_GOLD_IMPORT_DUTY", "Gold import duty", "+5 pp"),
    ("P_FERT_SUBSIDY", "Fertiliser subsidy generosity", "+1 = higher subsidy"),
    ("P_SUGAR_ETHANOL", "Sugar export / ethanol blending policy", "+1 = more favourable to millers"),
    ("P_IRDAI_REG", "Insurance regulation tightening (IRDAI)", "+1 = tightening"),
    ("P_POWER_REFORM", "Power market / DISCOM reform", "+1 = reform progress"),
    ("P_MINING_ROYALTY", "Mining royalty / mineral tax burden", "+1 = higher"),
    ("P_LABOUR_CODES", "Labour code implementation cost", "+1 = implementation"),
    ("P_INFRA_SPENDING_ROADS", "Road/highway awarding", "+10%"),
    ("P_HOUSING_POLICY", "Affordable-housing / home-loan support", "+1 = stronger support"),
    ("P_CAPITAL_GAINS_TAX", "Capital-gains / securities tax burden", "+1 = higher"),
    ("P_FDI_RULES", "FDI liberalisation", "+1 = liberalisation"),
]

COUNTRIES = [
    ("C_USA", "United States demand / relations", "+1 pp US demand growth"),
    ("C_CHINA", "China (demand and competition)", "+1 pp China growth"),
    ("C_EU_UK", "Europe and UK demand", "+1 pp demand growth"),
    ("C_GCC", "Gulf Cooperation Council economies", "+1 pp growth"),
    ("C_RUSSIA", "Russia (oil discounts, defence, sanctions)", "+1 = closer trade access / larger discounts"),
    ("C_SOUTH_SE_ASIA", "South & South-East Asia demand", "+1 pp growth"),
    ("C_AFRICA_LATAM", "Africa & Latin America demand", "+1 pp growth"),
    ("C_JAPAN_KOREA", "Japan & Korea (supply chains, capital)", "+1 pp growth"),
    ("C_MIDEAST_CONFLICT", "Middle East conflict intensity", "+1 = escalation"),
    ("C_INDIA_PAKISTAN", "India–Pakistan tension", "+1 = escalation"),
    ("C_RED_SEA", "Red Sea / Suez shipping disruption", "+1 = disruption"),
    ("C_US_CHINA_DECOUPLING", "US–China trade decoupling", "+1 = more decoupling"),
]

THEMES = [
    ("T_GENAI_SERVICES", "GenAI substitution of IT/BPO labour (higher = more substitution)", "+1"),
    ("T_CHINA_PLUS_ONE", "China+1 manufacturing relocation to India", "+1"),
    ("T_ENERGY_TRANSITION", "Energy transition investment", "+1"),
    ("T_PREMIUMISATION", "Consumer premiumisation", "+1"),
    ("T_FINANCIALISATION", "Household savings shift to financial assets", "+1"),
    ("T_QUICK_COMMERCE", "Quick-commerce disruption of retail/FMCG distribution", "+1"),
    ("T_DATA_CENTRES_IN", "Indian data-centre build-out", "+1"),
    ("T_GLP1", "GLP-1 / obesity drug adoption", "+1"),
    ("T_DEFENCE_EXPORTS", "Indian defence exports", "+1"),
    ("T_GRID_ELECTRIFICATION", "Grid & electrification capex", "+1"),
    ("T_FORMALISATION", "Formalisation of the economy", "+1"),
    ("T_DIGITAL_PAYMENTS", "Digital payments / UPI disruption of incumbents", "+1"),
]

INDUSTRIES = [
    ("I_PRIVATE_BANKS", "Private banks"), ("I_PSU_BANKS", "Public sector banks"),
    ("I_NBFC_VEHICLE_CONSUMER", "NBFC – vehicle/consumer/diversified"), ("I_HOUSING_FINANCE", "Housing finance"),
    ("I_MICROFINANCE", "Microfinance / small finance"), ("I_GOLD_LOANS", "Gold-loan NBFCs"),
    ("I_INFRA_POWER_FINANCE", "Infrastructure & power finance (PFC/REC/IRFC)"),
    ("I_LIFE_INSURANCE", "Life insurance"), ("I_GENERAL_INSURANCE", "General / health insurance"),
    ("I_AMC_WEALTH_BROKING", "Asset management, wealth, broking"), ("I_MARKET_INFRA", "Exchanges, depositories, RTAs"),
    ("I_IT_SERVICES", "IT services"), ("I_SOFTWARE_PLATFORMS", "Software products / engineering R&D services"),
    ("I_PHARMA_US_GENERICS", "Pharma – US generics exporters"), ("I_PHARMA_DOMESTIC", "Pharma – domestic branded"),
    ("I_CDMO_API", "CDMO / API manufacturing"), ("I_HOSPITALS_DIAGNOSTICS", "Hospitals & diagnostics"),
    ("I_AUTO_PV", "Passenger vehicles"), ("I_AUTO_2W", "Two-wheelers"), ("I_AUTO_CV_TRACTOR", "Commercial vehicles & tractors"),
    ("I_AUTO_COMPONENTS", "Auto components & tyres"), ("I_STEEL", "Steel"), ("I_NONFERROUS", "Aluminium, zinc, copper"),
    ("I_MINING", "Mining (coal, iron ore)"), ("I_OIL_UPSTREAM", "Oil & gas upstream"),
    ("I_REFINING_OMC", "Refining & oil marketing"), ("I_GAS_DISTRIBUTION", "Gas transmission & city gas"),
    ("I_POWER_THERMAL", "Thermal power generation"), ("I_RENEWABLES", "Renewable power"),
    ("I_POWER_GRID", "Power transmission & distribution utilities"),
    ("I_CAPITAL_GOODS", "Capital goods & electrical equipment"), ("I_DEFENCE", "Defence & aerospace"),
    ("I_RAILWAYS", "Railway equipment & PSUs"), ("I_CONSTRUCTION_EPC", "Construction / EPC"),
    ("I_CEMENT", "Cement"), ("I_REAL_ESTATE", "Real estate developers"),
    ("I_BUILDING_MATERIALS", "Building materials (pipes, tiles, wires, paints)"),
    ("I_CONSUMER_DURABLES", "Consumer durables & electricals"), ("I_FMCG_STAPLES", "FMCG staples & foods"),
    ("I_ALCOHOL_TOBACCO", "Alcohol & tobacco"), ("I_RETAIL", "Retail (apparel, grocery, department)"),
    ("I_QSR_FOOD_SERVICES", "QSR / food services"), ("I_JEWELLERY", "Jewellery"), ("I_TEXTILES", "Textiles"),
    ("I_CHEMICALS_SPECIALTY", "Specialty chemicals"), ("I_CHEMICALS_FERTILISER", "Commodity chemicals & fertilisers"),
    ("I_AGROCHEMICALS", "Agrochemicals"), ("I_TELECOM", "Telecom operators & towers"),
    ("I_AVIATION", "Aviation & airports"), ("I_LOGISTICS_PORTS", "Logistics, shipping & ports"),
    ("I_HOTELS_TRAVEL", "Hotels & travel"), ("I_INTERNET_PLATFORMS", "Internet platforms (food delivery, e-commerce, fintech)"),
    ("I_ELECTRONICS_EMS", "Electronics manufacturing services"), ("I_CONGLOMERATE", "Diversified conglomerates"),
    ("I_MEDIA_ENTERTAINMENT", "Media & entertainment"),
]


def build():
    nodes = []
    for i, n, s, y in FACTORS:
        nodes.append({"id": i, "type": "FACTOR", "name": n, "ssu": s, "series": y})
    for i, n, s in POLICIES:
        nodes.append({"id": i, "type": "POLICY", "name": n, "ssu": s, "series": None})
    for i, n, s in COUNTRIES:
        nodes.append({"id": i, "type": "COUNTRY", "name": n, "ssu": s, "series": None})
    for i, n, s in THEMES:
        nodes.append({"id": i, "type": "THEME", "name": n, "ssu": s, "series": None})
    for i, n in INDUSTRIES:
        nodes.append({"id": i, "type": "INDUSTRY", "name": n, "ssu": "+1 = 10% shift in industry profit pool", "series": None})
    uni = list(csv.DictReader(open(os.path.join(HERE, "data", "raw", "nifty200.csv"))))
    n50 = {r["Symbol"] for r in csv.DictReader(open(os.path.join(HERE, "data", "raw", "nifty50.csv")))}
    nx50 = {r["Symbol"] for r in csv.DictReader(open(os.path.join(HERE, "data", "raw", "niftynext50.csv")))}
    for r in uni:
        tier = "NIFTY_NEXT_50" if r["Symbol"] in nx50 else ("NIFTY_50" if r["Symbol"] in n50 else "MIDCAP_100")
        nodes.append({"id": r["Symbol"], "type": "COMPANY", "name": r["Company Name"], "ssu": "% equity value",
                      "series": r["Symbol"] + ".NS", "nse_industry": r["Industry"], "tier": tier, "isin": r["ISIN Code"]})
    os.makedirs(os.path.join(HERE, "graph"), exist_ok=True)
    json.dump(nodes, open(os.path.join(HERE, "graph", "nodes_seed.json"), "w"), indent=1)
    from collections import Counter
    print(len(nodes), Counter(n["type"] for n in nodes), Counter(n.get("tier") for n in nodes if n["type"] == "COMPANY"))


if __name__ == "__main__":
    build()
