#4. Write a python program to create a function which expects kwargs arguments.
def Address(**data):
    for i,j in data.items():
        print(i,j);

Address(name='Ankur',city='bahraich',Mob=9415113079)
