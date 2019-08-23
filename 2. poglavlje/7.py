def jedanDvaTri():
    brojac = ["Jedan",
              "Dva",
              "Tri"]

    while True:
        for e in brojac:
            yield e


g = jedanDvaTri()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
