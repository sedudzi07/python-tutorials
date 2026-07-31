first_name = "Ernest"

last_name = "Hackman"

full_name = first_name +" " + last_name

print("hello " + full_name)



course = "Programming with python"
#to change all sentence to block letters
print(course.upper())
#to change all letters to lower case
print(course.lower())

print(len(course))


#to find the index of a letter
print(course.find('P'))

#to find the index of a word. As in the beginning of the letter of the word 
print(course.find('python'))

#to replace a word in the sentence
print(course.replace("python", "Java"))

#Remeber that Python is case sensitive
print('python' in course)