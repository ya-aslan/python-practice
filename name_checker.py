name = input("Please enter a name:")

if len(name) > 6:
    print(name + " is a long name")
elif len(name) == 6:
    print(name + " is a medium name")
else:
    print(name + " is a short name")
