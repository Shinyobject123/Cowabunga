# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
# d) Make a list of all positive numbers in my_list below.

my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
list_a = [x for x in range(1, 101)]
print(list_a)
list_b = [x for x in range(20, 41) if x % 2 == 0]
print(list_b)
list_c = [x ** 2 for x in range(1, 101)]
print(list_c)
list_d = [x for x in my_list if x > 0]
print(list_d)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list

from number_list import num_list
print([num_list[x] for x in range(len(num_list)-5, len(num_list))])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
# Find and print the lowest number in num_list (1pt)
# Find and print the average of num_list (2pts)
# Remove the lowest number from num_list (2pt)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
print(max(num_list))
print(min(num_list))
print(sum(num_list)/len(num_list))
(num_list).sort()
num_list.pop(0)
top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

my_count = [num_list.count(x) for x in num_list]
print(my_count)
print(num_list[my_count.index(max(my_count))])


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
# Find the number of palindromes
# Hint: This may be easier to do with strings
#
pali_count = 0
for x in range(len(num_list)):
    t = str(num_list[x])
    if t[0] == t[3] and t[2] == t[1]:
        pali_count += 1
print(pali_count)



