
name = str(input("Enter your name: "))

while name == "":
    print("You have not entered name")

    name = input("Enter your name: ")





age = int(input("Enter your age: "))

while age < 0:
    print("Your age cannot be a negative number. Enter a valaid age.")

    age = int(input("Enter your age: "))

Hometown = input("Enter the name of your hometown: ")
while Hometown == "":
    print("So you want to tell us you dont have a home town?")

    Hometown = input("Enter the name of your hometown: ")

height = input("Enter your height in inches: ")

while height == 0:
    print("You cannot have that height ")
    height = input("Enter your height in Inches: ")


food = input("what food do you like? (q to quit): ")
while not  food == 'q':
    print(f"You like {food}")
    food = input("enter another food you like: (q to quit): ")

print("bye")



print(f'Hello {name}')
print(f"You are {age} years old")
print(f"You come from {Hometown}")
print(f"You are {height} inches tall")


  