''' Calculator'''

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# operator = input("Enter operator (+, -, *, /): ")

# if(operator == "+"):
#     print("Result : ", num1 + num2)
# elif(operator == "-"):
#     print("Result : ", num1 - num2)
# elif(operator == "*"):
#     print("Result : ", num1 * num2)
# elif(operator == "/"):
#     if(num2 != 0):
#         print("Result : ", num1 / num2)
#     else:
#         print("Error : Cannot divide by Zero")
# else:
#     print("ERROR : INVALD OPERATOR")

# ======================================================

# Assignment 2 - Number Guessing Game

# import random

# secrete_number = random.randint(1, 100)
# while(True):
    
#     guess = int(input("Guess the number between 1 to 100 : "))

#     if(guess > secrete_number):
#         print("Number is to High, Try Again...")

#     elif(guess < secrete_number):
#         print("Number is to Low, Try Again...")

#     else:
#         print("congratulation! Correct Guess")
#         break

#=======================================================

# Assignment 3 - Student Grade Calculator


# math = float(input("Enter Math Marks : "))
# science = float(input("Enter science Marks : ")) 
# english = float(input("Enter English Marks : "))
# history = float(input("Enter History marks: "))
# computer = float(input("Enter Computer marks: "))

# total = math + science + english + history + computer
# percentage = total / 5

# grade = ""

# if(percentage >= 90):
#     grade = "A"
# elif(percentage >= 80):
#     grade = "B"
# elif(percentage >= 70):
#     grade = "C"
# elif(percentage >= 60):
#     grade = "D"
# else:
#     grade = "F"

# print("\n----Result----")
# print("Total Marks : ", total)
# print("Percentage : ", percentage)
# print("Grade : ", grade)

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\nTotal:", total)
print("Percentage:", percentage)
print("Grade:", grade)