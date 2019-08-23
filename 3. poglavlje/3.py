try:
    a = int(input("Unesite vrijednost a: "))
    b = int(input("Unesite vrijednost b: "))
    c = int(input("Unesite vrijednost c: "))

    rezultat = (a + b) / c
    print(rezultat)
except ValueError:
    print("Iznimka - ValueError")
except ZeroDivisionError:
    print("Iznimka - ZeroDivisionError")
except:
    print("Ostale iznimke!")
