from array import *

# 1. Create an array and traverse.
arr1 = array('i', [1,2,3,4,5,6])
for i in arr1:
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
print(arr1[0])

# 3. Append any value to the array using append() method
print("step 3")
arr1.append(7)
print(arr1)

# 4. Insert value in an array using insert () method
print("Step 4")
arr1.insert(0, 0)
print()

# 5. Extend python array using extend() method
print("Step 5")

arr2 = array('i', [10,25,12])
arr1.extend(arr2)

print(arr1)

# 6. Add items from list into array using fromlist() method
print("step 6")
tempList = [67, 68,69]
arr1.fromlist(tempList)
print(arr1)

# 7. Remove any array element using remove() method
print("Step 7")
arr1.remove(3)
print(arr1)


#  8. Remove last array element using pop() method
print("Step 8")
arr1.pop()
print(arr1)

#  9. Fetch any element through its index using index() method

print("Step 9")
arr1.index(67)
print(arr1)

# 10. Reverse a python array using reverse() method 
print("Step 10")
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method

print("Step 11")
print(arr1.buffer_info())

# 12. check for number of occurrences of an element using count() method
print("Step 12")
arr1.append(0)
print(arr1.count(0))

# 13. Convert array tto string using tostring() method
    # This Didn't work forsome reason
            # print("Step 13")
            # strTemp = arr1.tostring()
            # print(strTemp)


# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(arr1.tolist())

# 15. Append a string to char array using fromstring() method



# 16. Slice elements from an array
print("Step 16")

print(arr1[0:3])

