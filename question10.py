#10. Write a python program to create a function to check whether a given number is even or odd.
a=int(input("Enter any number:"))
def Odd_Even(a): 
    if(a%2==0):
        print("Even",a)
    else:
        print("Odd",a)
Odd_Even(a)
a=int(input("Enter any number:"))
Odd_Even(a)
