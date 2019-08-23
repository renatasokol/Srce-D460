from collections import deque

red = deque()

while True:
    korisnik = input("Ime korisnika: ")
    if korisnik == "x":
        break
    vrsta = input("Vrsta korisnika (O ili P): ")
    if vrsta != "O" and vrsta != "P":
        print("Nepoznat tip korisnika!")
        continue
    red.append([korisnik, vrsta])

# Premium korisnici
broj = len(red)
i = 0
while i < broj:
    temp = red.popleft()
    if temp[1] == "P":
        print("Premium korisnik -", temp[0])
    else:
        red.append(temp)
    i += 1

# Obični korisnici
broj = len(red)
i = 0
while i < broj:
    temp = red.popleft()
    print("Običan korisnik -", temp[0])
    i += 1
