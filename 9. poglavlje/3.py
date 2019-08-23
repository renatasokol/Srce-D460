import csv

with open('podaci.csv', mode='w') as f:
    csvPisac = csv.writer(f,
                          delimiter=';',
                          doublequote=False,
                          escapechar="\\",
                          lineterminator="KRAJ\n",
                          quotechar="&",
                          quoting=csv.QUOTE_ALL)

    csvPisac.writerow(['Ime', 'Prezime',
                       'Grad, "PBR"'])
    csvPisac.writerow(['Pero', 'Peric',
                       'Zagreb, 10000'])
    csvPisac.writerow(['Maja', 'Majic',
                       'Split, 2100'])
    csvPisac.writerow(['Ivo', 'Ivic',
                       'Karlovac, 4700'])
