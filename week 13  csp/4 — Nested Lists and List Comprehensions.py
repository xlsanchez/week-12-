
list1 = [1,2,3]
print(list1[-1]) #Output: 1
list2 = [4,5,6]
print(list2[0]) # Output: 4 
# nested list
nested_list = [list1, list2]
print(nested_list[0]) # Output: 1,2,3
print(nested_list[1]) # Output: 4,5,6
print(nested_list[0][1])
print(nested_list[1][1])
print(nested_list[1][0])


fruits =["apple","orange","banana","coconut"]
vegetables = ["celery","carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[2][2])
print(groceries[1][1])
print(groceries[0][2])

for collection in groceries: 
    for food in collection:
        print(food, end=" ")
    print()


# num_pad() = ((1,2,3),
#              (4,5,6),
#              (7,8,9),
#              ("*", 0, "#"))\
#      for row in num_pad:
#         for num in row: 
#             print(num, end="")
#         print()



# # nested loop 
# for i in range(1,100001): #outer loop
#     for j in range(1,100001): #inner loop
#         if i > 0 and j > 0:
#          for k in range (1,100001):
#             print("in the number is " , i, j, k)






# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
     [10, 20, 30],
     [40,50,60],
     [70,80,90]
]




# Print the first list.
print(matrix[0])
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
sum_list = [row[-1] for row in matrix]

print(sum_list) #Output: {30,60,90}
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
# numbers from 1-10 using a comprehension 
squares = [x**2 for x in range(1,11)]
# for x in range (1,11):
# print(x**2)
print(squares)