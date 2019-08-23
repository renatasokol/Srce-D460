def zbrojiBrojeveDo(x):
    if x == 1:
        return 1
    else:
        return x + zbrojiBrojeveDo(x - 1)


zbroj = zbrojiBrojeveDo(5)
print(zbroj)
