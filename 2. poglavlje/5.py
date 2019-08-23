def izracun(a, b):
    def parniZbroj(a, b):
        return 2 * a + 5 * b

    def neparniZbroj(a, b):
        return a * b - 10

    if (a + b) % 2 == 0:
        return parniZbroj(a, b)
    else:
        return neparniZbroj(a, b)


rezultat = izracun(5, 15)
print(rezultat)
