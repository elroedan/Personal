from array import *

arr1 = array('i', [0, 10, 1,2,3,4])
print(arr1)

def findingIndexArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
        
    return "Value not in the given array!"


print(findingIndexArray(arr1, 10))