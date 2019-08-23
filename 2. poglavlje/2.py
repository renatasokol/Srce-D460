def brojParnihZnamenki(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1 + brojParnihZnamenki(int(x / 10))
    else:
        return brojParnihZnamenki(int(x / 10))


x = input("Unesite broj: ")
x = int(x)

broj = brojParnihZnamenki(x)
print(broj)
