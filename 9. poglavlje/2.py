import csv

with open("podaci.csv", "r") as f:
    csvCitac = csv.reader(f,
                          delimiter=';',
                          skipinitialspace=True)
    brojac = 0
    for row in csvCitac:
        if brojac == 0:
            znacenje = row
            brojac += 1
        else:
            print(znacenje[0], ": ", row[0], sep="")
            print(znacenje[1], ": ", row[1], sep="")
            print(znacenje[2], ": ", row[2], sep="")
            print(znacenje[3], ": ", row[3], sep="")
            print()
            brojac += 1
