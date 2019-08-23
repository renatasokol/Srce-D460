class Fakultet:
    brojac = 0

    def __init__(self, smjer):
        self.__smjer = smjer
        Fakultet.brojac += 1

    def brojStudenata():
        return Fakultet.brojac


class Student(Fakultet):
    def __init__(self, ime, prezime, smjer):
        super().__init__(smjer)
        self.__ocjene = []


s1 = Student("Pero", "Perić", "Smjer 1")
s2 = Student("Ivo", "Ivić", "Smjer 2")

print("Broj studenata je:", Fakultet.brojStudenata())
