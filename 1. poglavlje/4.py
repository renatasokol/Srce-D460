lista = [1, 2, 3, 4, 5, 6, 7]

broj = input("Unesite broj: ")
broj = int(broj)

for e in lista:
    if e == broj:
        print("Postoji!")
        break
else:
    print("Ne postoji!")
