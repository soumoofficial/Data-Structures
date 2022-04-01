# Programm to remove first occurence of a specified element from a list

class Removing:
    list1 = [1,2,3,4,4,1,3,3,2]

    item = int(input("Enter item to remove :"))
    list1.remove(item)
    print(list1)