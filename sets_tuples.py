#sets amd tuples examples 
#sets examples:
set1 = {1,2,3,4,5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

#sets drop duplicate items:
set2 = {"apple", "banana", "cherry", "cherry"}
print(set2) #{'apple' , 'banana', 'cherry'}

#tuples examples: 
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
#tuples are ommutable meanign they cant be changed aftrer creation 
# tuples useful for storing data that shouldnt be changed 

social_security_number = (123444, 4444445, 5676789)
print(social_security_number)