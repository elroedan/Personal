# 1. Create an array and traverse.

from array import *

my_array = array('i', [10, 11, 12, 13])
for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
my_array[2]
print(my_array)
# 3. Append any value to the array using append() method
print("Step 3")
my_array.append(14)
print(my_array)

# 4. Insert value in an array using insert () method

print("Step 4")
my_array.insert(0, 9)
print(my_array)

# 5. Extend python array using extend() method

print("Step 5")
arr1 = array('i', [20, 21, 22, 23])
my_array.extend(arr1)
print(my_array)

# 6. Add items from list into array using fromlist() method

print("STep 6")
my_list = [1, 2, 3]
my_array.fromlist(my_list)
print(my_array)

# 7. Remove any array element using remove() method

print("STep 7")
my_array.remove(10)
print(my_array)

#  8. Remove last array element using pop() method

print("Step 8")
my_array.pop()
print(my_array)

#  9. Fetch any element through its index using index() method

print("Step 9")
print(my_array.index(20))

# 10. Reverse a python array using reverse() method 

print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
''' Buffer gets the memory address and the length of the buffer that holds the array content
    Usualyy displays it in bytes
'''
print("Step 10")
print(my_array.buffer_info())

# 12. check for number of occurrences of an element using count() method

print("Step 12")
my_array.append(9)
print(my_array.count(9))

# 13. Convert array tto string using tostring() method

print("To string Not Working!!")
        # strValue = my_array.tostring()

# 14. Convert array to a python list with same elements using tolist() method

print("Step 14")
print(my_array.tolist())

# 15. Append a string to char array using fromstring() method

print("From string not working ")
# 16. Slice elements from an array


print("Step 16")
print(my_array[: 5])
