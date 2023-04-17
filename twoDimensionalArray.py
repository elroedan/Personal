import numpy as np

# For two dimensional use numpy
two_Dimensional_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


#  Inserting a value in a two D array
#  new_two_d = np.insert(name of array to insert, index , [[values]], axis= 1 for column 0 is row)
print("Inserted column")
new_two_c = np.insert(two_Dimensional_array, 0, [[1, 4, 7, 5]], axis=1)
# print(new_two_c)

print("Inserting row")
new_two_r = np.insert(two_Dimensional_array, 2, [[1, 4, 7, 5]], axis=0)
# print(new_two_r)

# Appendind value into two D array
# new_two_d = np.append(two_Dimensional_array, [[1, 4, 7, 5]], axis=1)
 
new_append = np.append(two_Dimensional_array, [[1, 4, 7, 5]], axis=0)
# print(new_append)

# print(two_Dimensional_array) 
# Acces an element of two D array
    # print(two_Dimensional_array[0,1])
    # print(two_Dimensional_array[2, 3])
    # print(two_Dimensional_array[0,1])

def accessElements(array, row_index, column_index):
    if row_index >= len(array) or column_index >= len(array[0]):
        print("Incorrect index")

    else: 
        print(array[row_index, column_index])

# accessElements(two_Dimensional_array, 3, 2)
# accessElements(two_Dimensional_array, 1, 3)

# Traverese a two D array

def traverseTDArray(array):
    # This is the length of the row 
    for i in range(len(array)):
    # This is the length of the column 
        for j in range(len(array[0])):
            print(array[i][j])

    
print(two_Dimensional_array) 

# traverseTDArray(two_Dimensional_array)

#  Searching a twoD array

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if value == array[i][j]:
                return (i,j)
    return "Not Found "

print(searchTDArray(two_Dimensional_array, 9 ))

#  deleting a column from two D array

def deleteColumnTDArray(array, value):
    x = np.delete(array, value - 1, axis=1)
    print(x)
def deleteRowTDArray(array, vlaue):
    x= np.delete(array, vlaue - 1, axis=0)
    print(x)

deleting_row = np.delete(two_Dimensional_array, 1, axis=0)
deleting_col = np.delete(two_Dimensional_array, 2, axis=1)
deleteColumnTDArray(two_Dimensional_array, 2)
deleteRowTDArray(two_Dimensional_array, 2)