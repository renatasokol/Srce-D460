class Vozilo:
    def __init__(self, proizvodac, model, godiste):
        self.proizvodac = proizvodac
        self.model = model
        self.godiste = godiste

    def ispis(self):
        print("Podaci o vozilu su:")
        print("Proizvođač:", self.proizvodac)
        print("Model:", self.model)
        print("Godište:", self.godiste, end="\n\n")


v1 = Vozilo("Porsche", "911", 2019)
v2 = Vozilo("Ferarri", "488", 2019)

v1.ispis()
v2.ispis()
