class Vozilo:
    def __init__(self, proizvodac, model, godiste):
        self.__proizvodac = proizvodac
        self.__model = model
        self.__godiste = godiste


v1 = Vozilo("Porsche", "911", 2019)

# Pokušaj dohvaćanja privatne varijable __proizvodac
print(v1.__proizvodac)
