def ispis(sudionici, rezultati):
    i = 0
    for s in sudionici:
        print(s, ":", rezultati[i])
        i += 1


sudionici = ["Ivica", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rezultati = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]

print("Prije sortiranja: ")
ispis(sudionici, rezultati)

brojElemenata = len(rezultati)
for i in range(brojElemenata - 1):

    zamjena = False
    for j in range(brojElemenata - 1 - i):
        if rezultati[j + 1] < rezultati[j]:
            rezultati[j], rezultati[j + 1] = \
            rezultati[j + 1], rezultati[j]
            sudionici[j], sudionici[j + 1] = \
            sudionici[j + 1], sudionici[j]
            zamjena = True

    if zamjena == False:
        break

print("\n\nNakon sortiranja: ")
ispis(sudionici, rezultati)
