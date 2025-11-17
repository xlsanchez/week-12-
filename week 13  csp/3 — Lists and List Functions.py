# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.\

# Collections are used to store multiple items in a single variable 
# list are ordered collections of items 
# list are mutable, meaning you can change their content
# list are created using square brackets []

list_of_fruits = ["apple", "banana" , "cherry", "date"]
print(list_of_fruits) #['apple' , 'banana' , 'cherry', 'date]
print(type(list_of_fruits)) #class 'list'>
# Accessing items in a list
print(list_of_fruits[0])#apple 
print(list_of_fruits[1])# banana
print(list_of_fruits[-1]) #date
print(list_of_fruits[1:3]) # ['banana' , 'cherry'] 
#reversing a list 
list_of_fruits.reverse()
print(list_of_fruits) #['date', 'cherry' , 'banana' , 'apple']
print(list_of_fruits[::-1]) #['apple' , ' banana' , 'cherry ' , 'date']
#Appending items to a list 
list_of_fruits.append("elderberry") #add items to the end of the list 
print(list_of_fruits)
list_of_fruits.extend(["fig", "grape", "honeydew"])
#add multiple items to the end of the list 
print(list_of_fruits)
list_of_fruits.reverse()
print(list_of_fruits.reverse)
#Poppign items from a list 
popped_item = list_of_fruits.pop()
#removes and returns the last item
print(popped_item) #honeydew
print(list_of_fruits)
# inserting items at a specific index 
list_of_fruits.insert(1,"blueberry")
print(list_of_fruits)
# removing a specific item by value 
list_of_fruits.remove("banana")
print(list_of_fruits)

list_of_fruits.insert(3,"starberry")
print(list_of_fruits)

list_of_fruits.sort() # sorts the list in ascending order
print(list_of_fruits)
#Why use lists? instead of individual variables 
#imagine you have 100 items to manage
list_of_items = list(range(1,101)) #creates a list of #
print(list_of_items)

list_of_items = list(range(1,1001))
print(list_of_items)
print(len(list_of_items))

list_of_items.extend(range(1000,2001))
print(list_of_items)