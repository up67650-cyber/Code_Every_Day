# Q1. Take two numbers as input from the user. Print their sum, difference,
# product, and remainder.

# num1 = int(input("Enter a number1:"))
# num2 = int(input("Enter a number2:"))

# print (num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 % num2)

# Q2. Take a year as input. Check if it is a leap year. A year is a leap
# year if it is divisible by 4, but not by 100, unless it is also
# divisible by 400.

# year = int(input("Enter a year:"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("It's a leap year")
# else:
#     print("Not a leap year")

# Q3.Take a list of names as input (comma separated). Split them, sort them
# alphabetically, and join them back with " | " as separator.

# names_input = "Dog,Deer,Lion,Cat,Boy"
# word = names_input.split(",") 
# print(" | ".join(word))


# Q2: Take a number as input. Print whether it is even or odd using the %
# operator and a comparison operator.
# num1 = int(input("Enter a number:"))
# print(num1 % 2 == 0)

# Q3: Take the user's age as input. Check and print whether they are eligible
# to vote (age >= 18) and whether they are a senior citizen (age >= 60).
# Print both results.

# age =  int(input("Enter your age:"))
# voter = age >= 18
# senior_citizens = age >= 50
# print (f"You are eligible =  {voter}")
# print(f"You are senior citizens = {senior_citizens}")

# Q4: A student scored marks in 3 subjects. Take all three as input,
# calculate the total and average, and print both using an f-string.

# Bio = int(input("Enter a marks:"))
# Chem = int(input("Enter a marks:"))
# Phy = int(input("Enter a marks:"))
# Total = Bio + Chem + Phy
# Average = (Total / 3)
# print(f"total marks is {Total} and average marks {Average}")

# Q5.Take a number as input. Print whether it is positive, negative, or zero.
# Num = int(input("Enter a number:"))
# if Num > 0:
#     print("Positive")
# elif Num < 0:
#     print("Negative")
# else:
#     print("Zero")

# Q8: Take two numbers as input. Print the greater of the two. If they are
# equal, print "Both are equal."

# num1 = int(input("Enter a number 1:"))
# num2 = int(input("Enter a number 2:"))
# if num1 > num2:
#     print(f"{num1} grater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num2}")
# else:
#     print("Both are equal")

# Take a student's marks as input. Print their grade based on this scale:
# 90 and above → A
# 75 to 89 → B
# 60 to 74 → C
# 40 to 59 → D
# Below 40 → F


# marks = int(input("Enter a number:"))
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif  marks >= 60:
#     print("C")
# elif marks >= 40:
#     print("D")
# else:
#     print("Fail")

# Q11. Print all the numbers which are divisible by 3 and 5, from 1 to 100.
# num = int(input("Enter a number:"))
# while num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)
#     num += 1

# Q12 Sum of all the numbers from 1 to 100.
# start = int(input("Enter a number"))
# end = int(input("Enter a number"))
# i = start
# total = 0
# while i  <= end:
#     total = total + i
#     i += 1

#     print(f"total = {total}")


# Q13 Sum of all the numbers from 1 to 100 divisible by 2 and 7.
# start = int(input("Enter a number"))
# end = int(input("Enter a number"))
# i = start
# total = 0
# while i  <= end:
#     if i  % 2 == 0 and i % 7 == 0:
#         total = total + i
#     i += 1

#     print(f"total = {total}")

# Ask a number from the user, print the multiplication table upto 10.

# n  = int(input("Enter a number:"))
# i = 1
# while i < 11:
#     print(f"{n} * {i} = {n*i}")
#     i += 1



#      PATTERN 

# Q15 Print this patter 
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1, i + 1):
#         print("*", end = '')
#     print()

# Q16 Print this pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range (1 ,6):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# Q17 Print this patter
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end = " ")
#     print()

# Q18 Print this pattern
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for i in range(5, 0, -1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# Q19 Print this patter
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# n = 5
# for i in range(1 , n+1):
#     for j in range(n,i-1,-1):
#         print(j,end = " ")
#     print()