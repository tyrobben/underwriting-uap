### user\_input

Commercial grading contractor grading land for commercial buildings. Some work for apartment buildings. Located in Redding, California, 25 employees, 5,000,000 gross receipts, no past losses.  Has 2 light trucks, 5 extra heavy trucks and 3 private passenger vehicles.

### retrieved\_context

SRC1: "BEST'S HAZARD INDEX – Grading of Land: Autombile Liability 6, General Liability: Premises and Operations 7, General Liability: Products - Completed Operations 6. Appetite: ACCEPTABLE.\nNAICS 238891 238910 | ISO GL 95410"
SRC2: "Carrier GL guideline: not excluded class unless tract or condominium work
SRC3: "Carrier Underwriting Notes: add earth movement exclusion if grading contractor in San Diego County

### expected\_json

{
  "naics": ["238910", "23891"],
  "sic": ["1629","1611", "1794"],
  "am_best_class": "Grading of Land",
  "iso_gl": [
    { "code": "95410", "desc": "Grading of Land" }
  ],
  "vehicle_types": [
    { "type": "Light Truck",        "count": 2 },
    { "type": "Extra Heavy Truck",  "count": 5 },
    { "type": "Private Passenger",  "count": 3 }
  ],
  "appetite_flag": "Quote",
  "citations": ["SRC1", "SRC2", "SRC3"]
}