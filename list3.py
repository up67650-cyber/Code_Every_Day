# Q1. Given a list, remove all duplicate elements while preserving the original
# order of the unique items.

# def remove_duplicates(lst):
#     result = []
#     for num in lst:
#         if num not in result:
#             result.append(num)
#     return result
# nums = [1, 5, 4, 5, 5, 6, 5, 4, 3, 5, 6, 7, 6, 7, 1, 1, 1]
# print(remove_duplicates(nums))


# Q2.Separate a list of integers into two distinct lists: one containing all the
# even numbers and the other containing all the odd numbers.

# def even_odd_list(lst):
#     even_list = []
#     odd_list = []
#     for num in lst:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)
#     print(f"Even numbers are {even_list}")
#     print(f"Odd numbers are {odd_list}")

# num = [1,22,13,26,34,54,334,22,37,67,564,32,23]
# even_odd_list(num)

# Q3.Q63. Create a list containing the squares of numbers from
# 1 to 10 (i.e., [1, 4, 9, ..., 100]).

# result = []
# for i in range(1,11):
#     result.append(i ** 2)

# print(result)


# Q4.Given a list of numbers (which may contain duplicates), write a Python script
# that takes an integer as input from the user and removes all occurrences of that
# integer from the list.

# def remove_occurance(lst,target):
#     while target in lst:
#         lst.remove(target)

# nums = [1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 5, 6, 4, 1, 7, 8, 1]
# print(f"target removed {nums}")

# Q5. Write a Python script that iterates through a list of integers and replaces every
# negative number found in the list with the value 0.

# def replace_negative(lst):
#     n = len(lst)
#     for i in range (n):
#         if lst[i] < 0:
#             lst[i] = 0
#     return lst

# nums = [1, 4, -1, -45, -100, 6, 7, 8, -1]
# print(replace_negative(nums))