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
for i in range(brojElemenata):

    minIndex = i
    for j in range(i + 1, brojElemenata):
        if rezultati[j] < rezultati[minIndex]:
            minIndex = j

    rezultati[i], rezultati[minIndex] = rezultati[minIndex], rezultati[i]
    sudionici[i], sudionici[minIndex] = sudionici[minIndex], sudionici[i]

print("\n\nNakon sortiranja: ")
ispis(sudionici, rezultati)
