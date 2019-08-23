def bottles(brojBoca=99, nazivNapitka="beer"):

    brojBocaNaPocetku = brojBoca

    while brojBoca >= 0:

        if brojBoca >= 2:
            yield (str(brojBoca) + " bottles of " +
                   nazivNapitka + " on the wall, " +
                   str(brojBoca) + " bottles of " +
                   nazivNapitka + ".\n" +
                   "Take one down and pass it around, " +
                   str(- 1) + " bottles of " +
                   nazivNapitka + " on the wall.\n")

        elif brojBoca == 1:
            yield (str(brojBoca) + " bottle of " +
                   nazivNapitka + " on the wall, " +
                   str(brojBoca) + " bottle of  " +
                   nazivNapitka + ".\n" +
                   "Take one down and pass it around, " +
                   "no more bottles of " +
                   nazivNapitka + " on the wall.\n")


        else:
            yield ("No more bottles of " + nazivNapitka +
                   " on the wall, no more bottles of " +
                   nazivNapitka + ".\n" +
                   "Go to the store and buy some more, "
                   + str(brojBocaNaPocetku) +
                   " bottles of " +
                   nazivNapitka + " on the wall.")

        brojBoca -= 1

g = bottles(4)

for e in g:
    print(e)
