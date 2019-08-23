from abc import ABC, abstractmethod


class Citati:
    def __init__(self):
        self._pretplatnici = set()
        self._danasnjiCitat = None

    def noviPretplatnik(self, pretplatnik):
        self._pretplatnici.add(pretplatnik)
        pretplatnik._izvor = self

    def _obavijesti(self):
        for p in self._pretplatnici:
            p.osvjezi(self._danasnjiCitat)

    @property
    def danasnjiCitat(self):
        return self._danasnjiCitat

    @danasnjiCitat.setter
    def danasnjiCitat(self, value):
        self._danasnjiCitat = value
        self._obavijesti()


class Pretplatnik(ABC):
    def __init__(self):
        self._izvor = None
        self._danasnjiCitat = None

    @abstractmethod
    def osvjezi(self, value1):
        pass


class KonkretanPretplatnik(Pretplatnik):

    def __init__(self, naziv):
        super().__init__()
        self._naziv = naziv

    def osvjezi(self, danasnjiCitat):
        self._danasnjiCitat = danasnjiCitat
        print("Pretplatnik", self._naziv,
              "je primio novi citat")
        print("  Citat =", self._danasnjiCitat)


c = Citati()
p1 = KonkretanPretplatnik("Ivica")
p2 = KonkretanPretplatnik("Marica")

c.noviPretplatnik(p1)
c.noviPretplatnik(p2)
c.danasnjiCitat = "Brod je siguran u luci, ali brod nije izgađen da bi bio u luci."
print()
c.danasnjiCitat = "Budi promjena koju želiš vidjeti u svijetu."
print()
c.danasnjiCitat = "Nikada nije prekasno da budete ono što bi mogli biti."
