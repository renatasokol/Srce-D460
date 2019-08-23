def jeProst(broj):
    def jeProstInner(broj, i):
        if broj == i:
            return 1
        if broj % i == 0:
            return 0
        return jeProstInner(broj, i + 1)

    return jeProstInner(broj, 2)


if jeProst(7) == 1:
    print("Prost je!")
else:
    print("Nije prost!")
