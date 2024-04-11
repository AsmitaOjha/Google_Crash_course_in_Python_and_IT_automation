# create any set anf try to use frozenset(setname)

# Find the elements in a given set that are not in another set

#     set1 = {1,2,3,4,5}
#     set2 = {4,5,6,7,8}

#     diffrence between set1 and set2 is {1,2,3}
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print('Original Sets: ')
print(set1)
print(set2)
print("Difference of set1 and set2 using difference(): ")
print(set1.difference(set2))
print("Difference of set2 and set1 using difference():")
print(set2.difference(set1))
print("Difference of set1 and set2 using - operator: ")
print(set1 - set2)
print("Difference of set2 and set1 using - operator:")
print(set2 - set1)