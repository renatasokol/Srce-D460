class Vozilo:
    def __init__(self, proizvodac, model, godiste):
        self.__proizvodac = proizvodac
        self.__model = model
        self.__godiste = godiste

    @property
    def proizvodac(self):
        return self.__proizvodac

    @proizvodac.setter
    def proizvodac(self, proizvodac):
        self.__proizvodac = proizvodac


v1 = Vozilo("Porsche", "911", 2019)

print(v1.proizvodac)
v1.proizvodac = "718"
print(v1.proizvodac)
