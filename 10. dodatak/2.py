from abc import ABC, abstractmethod


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
            self._sudionici = set()
            self._cijena = pocetnaCijena
            self._korak = korak
            self._pobjednik = None
            self._poziv = 0

    def dodajSudionika(self, sudionik):
        self._sudionici.add(sudionik)
        sudionik.setAukcija(self)
        sudionik.setCijena(self._cijena)

    def makniSudionika(self, promatrac):
        self._sudionici.discard(sudionik)
        sudionik._aukcija = None

    def _obavijesti(self):
        for s in self._sudionici:
            s.novaCijena(self._cijena)

    def _proglasenjePobjednika(self):
        print(">> Aukcija je završena!")
        print(">> Pobjednik je:", self._pobjednik)

    def poziv(self):
        if self._poziv < 2:
            print(">> ", self._poziv + 1,
                  ". poziv!", sep="")
            self._poziv += 1
        else:
            self._proglasenjePobjednika()

    def ponuda(self, ponuda, ponuditelj):
        if self._cijena + self._korak <= ponuda:
            self._cijena = ponuda
            self._pobjednik = ponuditelj.naziv
            self._poziv = 0
            print(">>", self._pobjednik,
                  "je ponudio cijenu.")
            print(">> Nova cijena je:",
                  self._cijena, "kn.")
            self._obavijesti()
        else:
            print(">>", ponuditelj.naziv,
                  "je ponudio cijenu.")
            print(">> Ponuda je odbijena! " +
                  "Premali korak cijene.")
            self._poziv += 1
            if self._poziv > 2:
                self._proglasenjePobjednika()


class Sudionik(ABC):
    def __init__(self):
        self.aukcija = None
        self.cijena = None

    @abstractmethod
    def novaCijena(self, cijena):
        pass

    @abstractmethod
    def ponudi(self, cijena):
        pass

    @property
    def cijena(self):
        return self._cijena

    @cijena.setter
    def cijena(self, value):
        self._cijena = value

    @property
    def aukcija(self):
        return self._aukcija

    @aukcija.setter
    def aukcija(self, value):
        self._aukcija = value


class Osoba(Sudionik):
    def __init__(self, naziv):
        super().__init__()
        self.naziv = naziv

    def novaCijena(self, ponuda):
        self.cijena = ponuda
        print(self.naziv, "je osvježio cijenu!")

    def ponudi(self, ponuda):
        if ponuda > self.cijena:
            self.aukcija.ponuda(ponuda, self)
        else:
            print("Ponuda nije viša od " +
                  "trenutno najviše ponude!")

    @property
    def naziv(self):
        return self._naziv

    @naziv.setter
    def naziv(self, value):
        self._naziv = value

    def setAukcija(self, aukcija):
        self._aukcija = aukcija

    def setCijena(self, cijena):
        self._cijena = cijena


aukcija = Aukcija.kreirajAukciju(100, 10)
aukcija2 = Aukcija.kreirajAukciju(100, 10)

ivica = Osoba("Ivica")
marica = Osoba("Marica")
perica = Osoba("Perica")

aukcija.dodajSudionika(ivica)
aukcija2.dodajSudionika(marica)
aukcija2.dodajSudionika(perica)

ivica.ponudi(110)
marica.ponudi(115)
ivica.ponudi(120)
aukcija.poziv()
perica.ponudi(150)
marica.ponudi(300)
aukcija.poziv()
aukcija.poziv()
aukcija.poziv()
