# Programm to concatenate dictionaries into a new one

class Con_Dict:
    dic1 = {1:10 , 2:20}
    dic2 = {3:30 , 4:40}
    dic3 = {5:50 , 6:60}

    dic2.update(dic3)
    dic1.update(dic2)

    print(dic1)


