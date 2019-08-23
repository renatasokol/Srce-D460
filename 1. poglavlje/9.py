nizZnakova = "Hello World!"
lista = [1, 2, 3, 4]

print("Niz znakova (petlja): ", end="")
i = len(nizZnakova) - 1
while i >= 0:
    print(nizZnakova[i], sep="", end="")
    i -= 1

print("\nLista (petlja): ", end="")
i = len(lista) - 1
while i >= 0:
    print(lista[i], sep="", end="")
    i -= 1

print("Niz znakova:", nizZnakova[::-1])
print("Lista:", lista[::-1])
