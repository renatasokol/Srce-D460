celsius = [0, 5, 10, 15.8]

fahrenheit = map(lambda x: (float(9) / 5) * x + 32, celsius)

print(list(fahrenheit))
