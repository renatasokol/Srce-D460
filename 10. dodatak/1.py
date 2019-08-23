class Aukcija:
    __aukcija = None

    @staticmethod
    def kreirajAukciju(pocetnaCijena, korak):
        if Aukcija.__aukcija == None:
            Aukcija(pocetnaCijena, korak)
        return Aukcija.__aukcija

    def __init__(self, pocetnaCijena, korak):
        if Aukcija.__aukcija != None:
            raise Exception("Može biti kreirana " +
                            "samo jedna aukcija!")
        else:
            Aukcija.__aukcija = self
            self._cijena = pocetnaCijena
            self._korak = korak

    @property
    def cijena(self):
        return self._cijena

    @property
    def korak(self):
        return self._korak


aukcija1 = Aukcija.kreirajAukciju(100, 10)
aukcija2 = Aukcija.kreirajAukciju(200, 20)

print(aukcija1)
print(aukcija2)

print(aukcija1.cijena)
print(aukcija2.cijena)
