# Programm to print the number of occurences of a specified element in a list

class Occurence :
    ele = [1,2,1,4,6,4,4,3,2,9,7,5]
    x = len(ele)
    find = int(input("Enter the element :"))
    count = 0
    for i in ele:
        if (find == i) :
            count += 1
    print(count)
