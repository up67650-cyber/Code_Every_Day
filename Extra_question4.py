# Check if a String Starts and Ends with the Same Vowel (Case Insensitive)
# Write a function starts_and_ends_with_same_vowel that takes a string as input and returns True if the string starts and ends with the same vowel (case insensitive), otherwise False.

# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# def starts_and_ends_with_same_vowel(s):
#     vowels = "aeiou"
#     if not s:
#         return False
#     first_char = s[0].lower()
#     last_char = s[-1].lower()
#     if first_char in vowels and last_char in vowels and first_char == last_char:
#         return True
#     return False
# a = "eye"
# print(starts_and_ends_with_same_vowel(a))


# Q2.Compare Last Digits
# Write a function compare_last_digits(num1, num2) that takes two integers as input and checks whether they have the same last digit.
# Return "same" if the last digits match, otherwise return "different".

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# def compare_last_digit(num1, num2):
#     num1 = str(num1)
#     num2 = str(num2)
#     if num1[-1] == num2[-1]:
#         return "same"
#     else:
#         return "different"

# a = 143
# b = 13
# print(compare_last_digit(a,b))


# Q3. Move Even Indices to End (Reversed)
# Given a tuple t, write a function move_even_indices_to_end_reversed to move all elements at even indices to the end of the tuple in reversed order, while keeping the odd-indexed elements in their original order.

# def move_even_indices_to_end_reversed(t):
#     odd = t[1::2]
#     even = t[::2][::-1]
#     return odd + even

# a = (10,20,30,40,50)
# print(move_even_indices_to_end_reversed(a))
