name = str(input("Enter youtr name: "))

if len(name) < 3:
    print("Name is too short, name must be at least three characters")

elif len(name)  > 50:
    print("Name is too long")

else:
    print("Name is okay")

age = int(input("Enter your age: "))

if age >= 18:
    print("you can vote")

else:
    print("you cannot vote")
