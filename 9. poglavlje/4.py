import json

data = {
    "ime": "Pero",
    "prezime": "Peric",
    "grad": "Zagreb"
}

with open("podaci.json", "w") as f:
    json.dump(data, f)
