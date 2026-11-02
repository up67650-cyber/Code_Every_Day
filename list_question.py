# Q1. Create list of number in which print  number on the basis of indexing have positive, negative and middle indexing
# number = [12,23,4,567,8,89,30,40,55,23,455,0] 
# n = len(number)
# print(f"First Positive indexing ={number[3]}")
# print(f"Second Negative indexing = {number[-2]}")
# print(f"Middle element ={number[n // 2]} ")

# Q2. Create a list of 5 numbers (e.g., [10, 20, 30, 40, 50]). Replace the second and
# fourth elements of this list with the number 0 using indexing.
# Print the updated list.

# number = [10, 20, 30, 40, 50]
# number[2] = 0
# number[4] = 0
# print(number)

# Q3.Given a list of numbers, write Python code using a loop to find and print the
# largest element. Do not use the built-in max() function.

# numbers = [12, 45, 7, 89, 23, 56, 34]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("The largest element is:", largest)

# Q4 Write a program that takes a list and a target number. Use a loop to determine if
# the target number exists in the list. Do not use the in operator.

# def contains_target(numbers, target):
#     for num in numbers:
#         if num == target:
#             return True
#     return False

# print(contains_target([12, 45, 7, 89, 23, 56, 34], 23))

# Q5. Odd and Even using Enumerate
# Given a list of integers, use enumerate() to print each number along with its index. Classify each as "Odd" or "Even" and print the result. Do not use the in operator or range(len()).
# numbers = [12, 45, 7, 89, 23, 56, 34, 12, 7]
# for index, num in enumerate(numbers):
#     if num % 2 == 0:
#         print(f"Index {index}: {num} is Even")
#     else:
#         print(f"Index {index}: {num} is odd")


# Q6. Max and Min using Indexing
# Given a list of numbers, find the index of the largest and smallest elements without using max(), min(), or index(). Print both values and their respective indices.
# max_index = 0
# min_index = 0

# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[max_index]:
#         max_index = i
#     if numbers[i] < numbers[min_index]:
#         min_index = i

# print(f"Largest element: {numbers[max_index]} at index {max_index}")
# print(f"Smallest element: {numbers[min_index]} at index {min_index}")

# Q7. Count using Indexing
# Given a list of numbers and a target value, count how many times the target appears in the list using only indexing (e.g., for i in range(len(list)) or enumerate). Do not use the .count() method or the in operator.

# target = 12
# count = 0

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count += 1

# print(f"Target {target} appears {count} times in the list.")