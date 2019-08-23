def danUTjednu():
    dani = ["Ponedjeljak",
            "Utorak",
            "Srijeda",
            "Četvrtak",
            "Petak",
            "Subota",
            "Nedjelja"]

    for e in dani:
        yield e


g = danUTjednu()

for e in g:
    print(e)
