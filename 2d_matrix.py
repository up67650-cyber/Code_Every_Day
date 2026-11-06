# Q1. Print 3 x 3 matrix addition
# matrix =  [
#     [2,3,4],
#     [3,1,7],
#     [7,8,9],
# ]
# total = 0
# for i in range(0,3):
#     for j in range(0,3):
#         total = total + matrix[i][j]

# print(total)

# Q2 performe matrix operation on 4 x 5

# matrix = [
#     [5, 7, 2, 3, 1],
#     [6, 3, 8, 1, 3],
#     [6, 4, 9, 0, 2],
#     [3, 6, 3, 8, 1],
# ]
# total = 0
# rows = len(matrix)
# columns = len(matrix[0])
# for i in range(0,rows):
#     for j in range(0,columns):
#         print(matrix[i][j], end = " ")
#     print()


# Q3.Given a 3x3 matrix, print its upper triangle.
# Replace all elements in the lower triangle (below the main diagonal) with an asterisk (*).

# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range (len(m)):
#         print(*["*" if i > j else m[i][j] for j in range(len(m))])


# Q4. Given a 3x3 matrix, print only the main diagonal elements and replace
# everything else with an asterisk (*).
# 1 2 3
# 4 5 6
# 7 8 9

# Expected Output:
# 1 * *
# * 5 *
# * * 9

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# rows = len(matrix)
# columns = len(matrix[0])
# for i in range(0,rows):
#     for j in range(0,columns):
#         if i == j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()