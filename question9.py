#9. Write a python program to create a function to check whether a number falls in a given range.
def test_range(n):
    
    if n in range(1,9):
        
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(8)
print()
test_range(11)

