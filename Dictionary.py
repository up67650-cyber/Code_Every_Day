#Q1. Remove Duplicate Characters from String
# Write a function remove_duplicates(s) that returns a new string with duplicate characters removed, preserving the original order of first appearance.

# def remove_duplicates(s):
#     seen = set()
#     result = []
#     for char in s:
#         if char not in seen:
#             seen.add(char)
#             result.append(char)
#     return''.join(result)

# a = "banana"
# print(remove_duplicates(a))

# Q2. Top Scorers
# Populate a dictionary with six student names and their corresponding marks.
# Loop through it and print the names of all students who achieved a score above 75.

# students = {
#     "Alice": 82,
#     "Bob": 67,
#     "Charlie": 91,
#     "Diana": 74,
#     "Eve": 88,
#     "Frank": 55,
# }
# for name,marks in students.items():
#     if marks >= 75:
#         print(f"Name:{name} ,Marks:{marks}")
    

# Q3.Dictionary Merge Function
# Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries
# (d1 and d2) as arguments and returns a new dictionary formed by merging them
# using the update() method. Ensure d1 remains unchanged.
# """

# def merge_dictionary(d1,d2):
#     new_dict = {}
#     new_dict.update(d1)
#     new_dict.update(d2)
#     return new_dict
# a1 = {"a": 1, "b": 2, "c": 3}
# a2 = {"d": 4, "e": 5, "f": 6}

# ans = merge_dictionary(a1,a2)
# print(ans)

# Q4 Sorting dictionary via key value pair

# marks = {"math": 85, "science": 92, "english": 90, "hindi": 78}
# ans = dict(sorted(marks.items(), key=lambda x: x[0]))
# print(ans)


# Q5. Sorting dictionary in descending order to get student marks.

# marks = {
#     "akshy": [43, 12, 98, 10, 22],
#     "priya": [76, 55, 34, 89, 61],
#     "rahul": [20, 45, 67, 30],
#     "sneha": [91, 73],
#     "karan": [38, 82, 47, 95, 29],
# }
# ans = dict(sorted(marks.items(), key = lambda x:sum(x[1]),reverse=True))
# print(ans)

# Q6 Sorting  dictionary to get student marks using name of students

# students = {
#     "anirudh": {"math": 87, "science": 92, "english": 74},
#     "priya": {"math": 65, "science": 78, "english": 90},
#     "rahul": {"math": 55, "science": 60, "english": 48},
#     "sneha": {"math": 95, "science": 88, "english": 82},
#     "karan": {"math": 70, "science": 45, "english": 63},
# }
# ans = dict(sorted(students.items(),key = lambda x:sum(x[1].values()),reverse = True))
# print(ans)