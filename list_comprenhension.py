#Q1. Using list comprehension, create a list of squares of all odd numbers from 1 to 20.

# new_list = [i * i for i in range(1,21)if i % 2 == 1]
# print(new_list)

# Q2 Given a list of marks, use list comprehension to create a new list that contains
# only the marks that are above 75.

# marks = [45, 87, 15, 94, 37, 89, 90, 99, 32, 11]
# new_list = [num for num in marks if num >= 75]
# print(new_list)

# Q3. From 1 to 100, make a list of all prime numbers.

# new_list = [n for n in range(2,101) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
# print(new_list)

