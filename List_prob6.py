# Programm to append the new item before the second element in an existing list.

from re import L


class New_Append :
     list1 = [1, 2 , 3 , 4]

     item = int(input("Enter item to append :"))

     list1.insert(1,item)
     print(list1)