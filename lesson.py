my_list = list(range(1,101))
# print(my_list)
# print(sum(my_list))
my_list.remove(67)
#  This method finds the missing number from 1- 100
def missingNumber(myList, totalCount):
    # TODO
    total = sum(myList)
    if totalCount == total:
        return True
    else:
        return totalCount - total
    

print(missingNumber(my_list, 5050))