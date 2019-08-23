def ucitajPaZbroji():
    try:
        a = int(input("Unesite vrijednost a: "))
        b = int(input("Unesite vrijednost b: "))
        c = int(input("Unesite vrijednost c: "))

        rezultat = a + b + c
        print("Zbroj je:", rezultat)
    except:
        print("Iznimka je uhvaćena u funkciji!")
        raise


try:
    ucitajPaZbroji()
except:
    print("Iznimka je uhvaćena u glavnom programu!")
