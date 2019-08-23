s = []
pomocniStog = []

while (len(s) < 10):
    x = int(input("Broj: "))
    s.append(x)

print(s)

while (len(s) > 0):
    temp = s.pop()
    if temp <= 5:
        pomocniStog.append(temp)

while (len(pomocniStog) > 0):
    s.append(pomocniStog.pop())

print(s)
