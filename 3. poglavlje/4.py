try:
    a = int(input("Unesite vrijednost a: "))
    b = int(input("Unesite vrijednost b: "))
    c = int(input("Unesite vrijednost c: "))

    rezultat = (a + b) / c
    print(rezultat)
except ValueError as e:
    print("Iznimka - ValueError, opis:", e)
except ZeroDivisionError as e:
    print("Iznimka - ZeroDivisionError, opis:", e)
except:
    print("Ostale iznimke!")
