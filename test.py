# from array import *
import random 

# # How to create an array
# # variable = array(ArrayType, [items])
# arr1 = array('i', [1,2,3,4,5,6])
# arr2 = array('d', [1.3, 1.5, 1.6])


# # arr1.remove(6)
# # print(arr1)

# # How to find the element in an array
# def accessElement(array, index):
#     if index >= len(array):
#         print("Error Boy")

#     else:
#         print(array[index]) 
# accessElement(arr1, 4)
# accessElement(arr1, 6)



# # How To search for the index of a value in an array
# def searchInArray(array, value):
#     for i in array:
#         if i == value:
#             return array.index(value)
        
#     return "Not Found!"
        
# # print(searchInArray(arr1, 4))

# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())

# a=[1,2,3,4,5]
# print(a[3:0:-1])




fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
print(fruit_list1) 
print(fruit_list2) 
print(fruit_list3) 
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
print(a[::3])

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")