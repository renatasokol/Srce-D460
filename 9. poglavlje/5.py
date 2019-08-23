import json

with open("podaci.json", "r") as f:
    data = json.load(f)

    placaSviSum = 0
    godinaSviSum = 0
    brojacSvi = 0

    godDevSum = 0
    brojacDev = 0

    for e in data["zaposlenici"]:
        placaSviSum += e["placa"]
        godinaSviSum += (2019 - e["godinaRodenja"])
        brojacSvi += 1

        if e["pozicija"].lower() == "developer":
            godDevSum += (2019 - e["godinaRodenja"])
            brojacDev += 1

    print("Prosjecna placa:",
          placaSviSum / brojacSvi)
    print("Prosjek godina:",
          godinaSviSum / brojacSvi)
    print("Prosjek godina programera:",
          godDevSum / brojacDev)
