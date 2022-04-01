# Programm to print keys and values separately and keys and value together iteratively

class Modify :
    dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    x = (dict1.keys())
    y = (dict1.values())
    

    for num in x:
        print(num,end=' ')
    for num1 in y:
        print(num1,end=' ')