### user\_input

Neighborhood dive bar with live music and karaoke, 75‑seat capacity, open 4 pm–2 am daily. Serves beer, wine, and spirits; no food service. Located in downtown Chicago. No formal security staff. One intoxication-related altercation in the past year. Owns a single passenger van for supply runs.

### retrieved\_context

SRC5: "BEST'S HAZARD INDEX – Bars, Taverns, Cocktail Lounges and Nightclubs: Liquor Liability 8, General Liability: Premises and Operations 7, General Liability: Products – Completed Operations 4, Property 7. Appetite: DECLINE for late‑night operations with limited security."
SRC6: "Carrier guideline: Decline risks where alcohol sales exceed 75 % of total receipts and closing time is after midnight."
SRC7: "SIC CODES AND CLASSIFICATIONS – 5813 Drinking Places (Alcoholic Beverages); NAICS 722410 Drinking Places (Alcoholic Beverages)."

### expected\_json

{
"naics": \["722410"],
"sic": \["5813"],
"am\_best\_class": "Bars, Taverns, Cocktail Lounges and Nightclubs",
"iso\_gl": \[
{ "code": "92451", "desc": "Bars or Taverns — no food service" }
],
"vehicle\_types": \[
{ "type": "Private Passenger", "count": 1 }
],
"appetite\_flag": "Decline",
"citations": \["SRC5", "SRC6", "SRC7"]
}
