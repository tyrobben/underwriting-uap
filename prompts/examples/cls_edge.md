### user\_input

Small craft brewery with an attached taproom (40 seats) that sells beer by the glass and offers limited food (pretzels, food‑truck partnerships). Annual production 3,000 barrels. No distribution—on‑premise sales only. Located in suburban Colorado; closes at 10 pm. Owns one light truck for grain pickup.

### retrieved\_context

SRC1: "Lines of Coverage → General Liability: Premises & Ops — Craft Breweries: Hazard Index 5 (Medium). Guidance: REFER if on‑premise consumption > 50 % of revenue."
SRC2: "BEST'S HAZARD INDEX – Craft Breweries, Microbreweries, and Brewpubs: Liquor Liability 6, GL Prem & Ops 5, Products‑Completed Ops 4. Appetite: REFER for operations with taproom seating > 25."
SRC3: "NAICS 312120 Breweries; SIC 2082 Malt Beverages. ISO GL 95310 Craft Brewery (Taproom)."

### expected\_json

{
"naics": \["312120"],
"sic": \["2082"],
"am\_best\_class": "Craft Breweries, Microbreweries, and Brewpubs",
"iso\_gl": \[
{ "code": "95310", "desc": "Craft Brewery — taproom" }
],
"vehicle\_types": \[
{ "type": "Light Truck", "count": 1 }
],
"appetite\_flag": "Refer",
"citations": \["SRC1", "SRC2", "SRC3"]
}
