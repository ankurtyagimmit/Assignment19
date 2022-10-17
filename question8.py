#8. Write a python program to multiply all the numbers in a list.
def mulList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1,2,3,4,5]
print("Multiple of given list is:",mulList(list1))
