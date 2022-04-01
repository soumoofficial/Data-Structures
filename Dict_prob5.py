# Programm to prepare a dictionary where the keys are numbers between 1 and 15 and the values are square of the keys.

class Prep :
    d = dict()
    for i in range(1,16):
        d[i] = i*i
    print(d)        