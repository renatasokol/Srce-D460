class NasumicniBroj:
    __instanca = None

    def __init__(self):
        if NasumicniBroj.__instanca != None:
            raise Exception("Singleton!")
        else:
            NasumicniBroj.__instanca = self
            NasumicniBroj.__sljedeci = 67

    @classmethod
    def broj(cls):
        if cls.__instanca == None:
            cls.__instanca = cls()

        tmp = cls.__sljedeci
        cls.__sljedeci = 9845612 % tmp + 17 * 7
        return tmp


print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
print(NasumicniBroj.broj())
