def prazan(stack):
    if len(stack) == 0:
        return True
    else:
        return False


def izbaci(stack):
    if prazan(stack) == False:
        temp = stack.pop()
        if (temp <= 5):
            izbaci(stack)
            stack.append(temp)
        else:
            izbaci(stack)


s = []

while (len(s) < 10):
    x = int(input("Broj: "))
    s.append(x)
print(s)
izbaci(s)
print(s)
