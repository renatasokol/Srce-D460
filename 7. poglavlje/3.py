from collections import deque

red = deque()

while True:
    korisnik = input("Ime korisnika: ")
    if korisnik == "x":
        break
    red.append(korisnik)

while len(red) > 0:
    print(red.popleft())
