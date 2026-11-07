# Q1. Compute Electricity Bill
# Write a function compute_electricity_bill that returns the electricity bill amount based on the number of units consumed.

# If the units consumed are less than or equal to 200, the cost per unit is 0.5.
# If the units consumed are less than or equal to 400, the cost per unit is 0.75 plus a fixed extra charge of Rs150.
# If the units consumed are more than 400, the cost per unit is 0.90 plus a fixed extra charge of Rs300.
# The function should return the total amount as a float.

# def compute_electricity_bill(units):
#     if units <= 200:
#         return units * 0.5
#     if units <= 400:
#         return units * 0.75 + 150
#     if units > 400:
#         return units * 0.90 + 300
# a = 200
# print(float(compute_electricity_bill(a)))
    


# Q2. Write a function that takes two strings, reverses the first string, concatenates it with the second string,
# and then check whether the concatenated string is palindrome or not

# def is_reverse_combined_palindrome(s1,s2):
#     otp_s1 = s1[::-1]
#     combined_string = otp_s1 + s2
#     return combined_string == combined_string[::-1]

# s1 = "hello"
# s2 = "olleh"
# print(is_reverse_combined_palindrome(s1,s2))
    
     
# Q3.Pangram Check
# Write a function is_pangram that takes a string text as input and returns True if the string is a pangram, False otherwise.

# A pangram is a sentence containing every letter of the alphabet at least once.

# import string

# def is_pangram(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     text_lower = text.lower()
#     for char in alphabet:
#         if char not in text_lower:
#             return False
#     return True

# Q4. Check for Arithmetic Progression
# Write a function is_arithmetic_progression(sequence) that takes a sequence of numbers as input and returns True if the sequence is an arithmetic progression, and False otherwise.

# An arithmetic progression is a sequence where the difference between consecutive terms is constant.

# def is_arithmetic_progression(sequnce):
#     if len (sequnce) < 3:
#         return True
#     diff = sequnce[1] - sequnce[0]
#     for i in range (2,len(sequnce)):
#         if sequnce[i] - sequnce[i-1] != diff:
#             return False
#     return True
# print(is_arithmetic_progression([1, 3, 5, 7, 9]))   # True (diff = 2)

            

