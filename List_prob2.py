# Write a programm to append a new item to the end of the list

class Appending_item :
    items = ["Soumo","Simran","Ayush","Sanjay","Jessica"]
    numbers = [1 , 2 , 3 , 4 , 5]
    num = int(input("Enter number to append :"))
    new_item = input("Enter the item to append :")
    
    numbers.append(num)
    print(numbers)
    items.append(new_item)
    print(items)