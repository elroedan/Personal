import numpy as np

def main():
    tempList = []
    userInput = int(input("How many day's temprature? "))
    count = 0
    while count != userInput:
        count += 1 
        dayTemp = int(input(f"Day {count}\'s high temp: "))
        tempList.append(dayTemp)


    print("Average = ", round(sum(tempList)/ len(tempList)))
    for temp in tempList:

        if temp > sum(tempList)/ len(tempList):
            print(f"Day {tempList.index(temp) + 1} temprature is above average")

    
# main()

my_array = list(range(1,101)) 

# print(my_array)

my_array.remove(72)
def findMissingNumber(array):
    
    sumList = 100*101/2
    sumMissingList = sum(array)

    print(sumList - sumMissingList)

# findMissingNumber(my_array)

list1 = [2,6,3,9,4, 4]
        # def TwoSum(list, target):
        #     for i in range(len(list)):
        #         if target - list[i] in list:
        #             return ([target - list[i], list[i]])
def TwoSum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                print(i, j)        
# TwoSum(list1, 13)

''' Finding if there are two integers the sum is a target '''
def OptimizedTwoSum(given_list, target):
    nums = {}
    
    for i, num in enumerate(given_list):
        if target - num in nums:
            print(nums[target - num], i)
            
        nums[num] = i
    print(nums[num])   
    print(nums)  

# OptimizedTwoSum(list1, 8)
'''Finding a number in an array'''
def findNumber(array, number):
     if number in array:
         print(array.index(number))

# findNumber(list1, 6)

'''How to find maximum product of two integers in the array where all elements are positive'''

max_product = 0
def findMaxProduct(array, max_product):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            test_product = array[i] * array[j]
            if test_product > max_product:
                max_product = test_product
                pairs = f"{array[i]}, {array[j]}"



    return (max_product, pairs)
list1 = [1,2,3,4,45,5,6,8]
# print(findMaxProduct(list1, max_product))

'''This is not the best solution I just looked at the big O on Max and it is O(n)'''
def optimizedFindMaxProduct(array):

    first_max_number = max(array)
    array.remove(first_max_number)
    second_max_number = max(array)
    

    return first_max_number * second_max_number, first_max_number, second_max_number


# print(optimizedFindMaxProduct(list1))
'''Thsi is my favorite way of finding the number of the two products and the numbers'''
def realOptimizedmaxProduct(array):

    array.sort()
    first_number = array[-1]
    second_number = array[-2]
    print(first_number * second_number)
    return first_number, second_number

# print(realOptimizedmaxProduct(list1))


# Check if there are any duplicates in a list ana return true or return false


list2 = [0, 9,2,3,4,5,53,2,2,3,5]
'''This is by far the fastest if you want to return true or false'''
def findDuplicates(array):
    return len(array) == len(set(array))

# print(findDuplicates(list2))

# Lets find the dublicate numbers
'''This is one of the best and simple ways to find the duplicates'''
def findDuplicateNumbers(array):
    duplicates = []    
    for i in array:
        if array.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    if len(duplicates) == 0:
        return "The List don't have duplicate numbers"
        
    return duplicates

print(findDuplicateNumbers(list2))

# Another method is 
'''Another good way to check unique or not'''
def isUnique(array):
    new_list = []
    duplicates = []
    for i in array:
        if i in new_list:
            duplicates.append(i)
            
        else:
            new_list.append(i)
    if len(duplicates) == 0:
        return False
    else:
        return duplicates

print(isUnique(list2))

#  Finding if two lists are equal
#  Rotate matrix

array = np.array([[0,1,2], [3,4,5], [6,7,8]])

def rotateArray(array):
    n = len(array)
    for layer in range(n//2):

        first = layer
        last = n - layer - 1
        for j in range(first, last):
            # Save top element
            top = array[layer][j]
            # move left eleement to top 
            array[layer][j] = array[-j-1][layer]
            # move bottom element left
            array[-j-1][layer] = array[-layer -1][-j-1]
            # move right to bottom
            array[-layer -1][-j-1] = array[j][-layer-1]
            # move bottom to right
            array[j][-layer-1] = top


    return array

print(array)
print(rotateArray(array))





