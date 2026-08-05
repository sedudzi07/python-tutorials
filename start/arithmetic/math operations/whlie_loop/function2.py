name = str(input("what is your name: " ))

print("Name: ", name)


age = int(input("what is your age?: "))

print("Age: ", age)

aggregate =int(input("Enter your aggregate"))
print("Your aggregate is:", aggregate)


if aggregate == 6:
    print("You will get your first choice")

elif 7 <= aggregate <= 9:

    print("You will get your second choice")

elif 10 <= aggregate <= 15:

    print("you shall get your third choice")

elif 16<= aggregate <= 20:
    print("you shall get your last choice")


else:
    print("you have failed register for next year")

