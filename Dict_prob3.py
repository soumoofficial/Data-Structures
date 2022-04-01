# Programm to check if a given key already exists in the dictionary

class Check_key:
    dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    key = int(input("Enter a key :"))
    x = dict1.keys()
    print(x)
    if key in x:
        print("key exist")
    else :
        print("Does not exist")