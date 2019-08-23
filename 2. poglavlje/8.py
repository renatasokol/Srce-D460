def prebroji(broj, znamenka):
    if broj == 0:
        return 0
    elif (broj % 10) == znamenka:
        return 1 + prebroji(broj // 10, znamenka)
    else:
        return prebroji(broj // 10, znamenka)


rezultat = prebroji(1223455, 2)
print(rezultat)
