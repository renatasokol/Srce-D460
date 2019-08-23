class Student:
    def __init__(self):
        self.ocjene = []

    def novaOcjena(self, ocjena):
        self.ocjene.append(ocjena)

    def aritmetickaSredina(self):
        suma = 0
        broj = 0
        for element in self.ocjene:
            suma += element
            broj += 1
        return suma / broj

    def brojOcjena(self, ocjena):
        return self.ocjene.count(ocjena)


s = Student()

s.novaOcjena(5)
s.novaOcjena(5)
s.novaOcjena(5)
s.novaOcjena(4)
s.novaOcjena(3)
s.novaOcjena(2)

print("Aritmeticka sredina je: ", s.aritmetickaSredina())
print("Sakupljenih ocjena (5) je:", s.brojOcjena(5))
