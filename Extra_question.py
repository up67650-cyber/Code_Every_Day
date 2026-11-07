# Q1.Check is even or divisible by 5
# Write a function is_even_or_divisible_by_5 that takes an integer as input and return True if it is even or is divisible by 5 else False.

# def is_even_or_divisible_by_5(num):
#     if num % 2 == 0 or num % 5 == 0:
#         return True
#     return False
# a = 4.3
# print(is_even_or_divisible_by_5(a))  


# Q2.Deinterleave Even and Odd Indices in String
# Write a function deinterleave that takes a string s as input and returns a new string where the characters at even indices are placed before the characters at odd indices.

# def deinterleave(s):
#     return s[::2] + s[1:2]

# a = "12345"
# print(deinterleave(a))

# Q3.Make dictionary from elements in index of lists
# Write a function make_dict_from_elems_in_index that returns a dictionary consisting of a single key-value pair formed as follows:

# the key is the element at the given index from the list keys.
# the value is the element at the given index from the list values


# def make_dict_from_elems_in_index(keys,values,index):
#     return {keys[index]:values[index]}

# a = {1:"apple",2:"ball",3:"cat"}
# print(make_dict_from_elems_in_index(list(a.keys()),list(a.values()),1))  


# Q4.Counts unique even and odd numbers
# Write a function count_unique_even_odd that takes list of integers, returns a dictionary with the count of unique even and odd numbers in the list.

# def count_unique_even_odd(lst):
#     unique_numbers = set(lst)
#     even_numbers = 0
#     odd_numbers = 0
#     for num in unique_numbers:
#         if num % 2 == 0:
#             even_numbers += 1
#         else:
#             odd_numbers += 1
#     return {"even":even_numbers,"odd":odd_numbers}

# num = 1,2,3,4,8,9,10,11,12
# print(count_unique_even_odd(num))


#Q5. Pattern Printing - W Pattern
# Given an integer n (where n > 0), print an "W" shaped pattern with n rows.

# The pattern should consist of a vertical bar (|) on the left and right sides of each row. Additionally, it should have forward slashes (/) and backslashes () moving diagonally towards each other from the top to the bottom.

# n = int(input("Enter the number of rows for the W pattern: "))
# for i in range (n):
#     print("|" + " "*(n-1-i)+"/"+" "*(2*i)+ "\\"+" " *(n-1-i) + "|")