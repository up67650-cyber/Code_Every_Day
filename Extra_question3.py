#Q1. Check If a Number is a Decreasing 4-Digit Number
# Write a function is_decreasing_number(n: int) -> bool that checks if a given 4-digit number is decreasing, meaning each digit is strictly less than the digit before it (from left to right).

# The function should return True if the number meets the criteria and False otherwise.

# def is_decreasing(n):
#     s = str(n)
#     return len(s) == 4 and all (s[i] > s[i + 1] for i in range)



#Q2. Double First and Last Elements in a List
# Write a function double_ends(l) that takes a list l (with at least two elements) and returns a new list where the first and last elements of l are duplicated at the beginning and end of the list, respectively.

# The new list should have:

# The first element of the original list inserted once at the beginning
# The last element of the original list inserted once at the end


# def double_ends(l):
#     return [l[0]] + l + [l[-1]

p = 9
q = 2
p = p % q
q = q ** p
p, q = q, p
print(q,p)