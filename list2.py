# Q1. Write a program that takes a list of numbers and, using a loop, determines
# whether it is sorted in ascending order. Print True if it is sorted,
# and False otherwise.

# def is_sorted(lst):
#     n = len(lst)
#     for i in range(0, n-1):
#         if lst[i] > lst[i+1]:
#             return False
#     return True

# nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]
# print(is_sorted(nums))

# Q2. Find the largest and smallest number in a list without using built-in functions
# like max() or min().

# def find_largest_smallest(lst):
#     if not lst:
#         return None, None

#     sorted_lst = sorted(lst)
#     return sorted_lst[-1], sorted_lst[0]


# numbers = [3, 1, 8, 4, 7, 2, 9, 5]
# largest, smallest = find_largest_smallest(numbers)
# print(f"Largest: {largest}, Smallest: {smallest}")

# Q3. Reverse a list without using the .reverse() method or list slicing ([::-1]).

# def reverse_list(lst):
#     n = len(lst)
#     new_list = []
#     for i in range(n-1,-1,-1):
#         new_list.append(lst[i])
#     return new_list
# nums = [1, 2, 34, 5, 6, 7, 8, 100]

# ans = reverse_list(nums)
# print(ans)

# Q4. Given two lists, merge them into a single new list without modifying the originals.

# def merge_two_list(lst1,lst2):
#     new_list = []
#     for num in lst1:
#         new_list.append(num)
#     for num in lst2:
#         new_list.append(num)
#     return new_list

# num1 = [1, 2, 3]
# num2 = [65,382,39]
# print(merge_two_list(num1,num2))


                    #  SLICING   #
# Q1. Given the list , what is the output of the following?
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[2:5])

# Q2.Given the list , what is the output of the following? step parameter


# b = [10, 20, 30, 40, 50, 60, 70, 80]
# print(b[1:8:2])

# Q3. Given the list , what is the output of the following? negative slicing

# c = ['A', 'B', 'C', 'D', 'E']
# print(c[-3:-1])
# print(c[::-1])
# print(c[0:-1:2])

# Q4. Given the list  what is the output of the following?
# e = [10, 20, 30]

# print(e[5:10])
# print(e[-5:-2])
