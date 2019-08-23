def paran():
    print("Paran!")


def neparan():
    print("Neparan")


broj = input("Unesite broj: ")
broj = int(broj)

(paran if broj % 2 == 0 else neparan)()
