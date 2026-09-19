
for x in range(1, 10):
    print(x)

print("we will now reverse the process")

for y in reversed(range(1, 21)):
    print(y)

print("now let us do skip a number in the range")

for number in range(1, 6):
    if number == 4:
        continue
    else:
        print(number)

print(" as you can see, 4 have been skipped")

print("now let us break out of the loop when we reacj a certain number")

tele = ("0531552185")
for tele in tele:
    if number == 2:
        break
    else:
        print(tele)
    