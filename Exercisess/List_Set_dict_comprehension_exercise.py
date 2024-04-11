#Create a Dictionary which contains the Binary values mapping
#  with numbers found in the below integer and binary and 
# save it in binary_dict.
integer =[0,1,2,3,4,5]
binary=["0",'1','10','11','100','101']
binary_dict={}
for i in range(len(integer)):
    binary_dict[integer[i]]=binary[i]
print(binary_dict)

#Create a List which contains additive inverse of a 
# given integer list. An additive inverse a for an integer i
#    is a number such that
integer = [1,2,3,6,7,-1,0,-5,-7]
additive_inverse=[-num for num in integer]
print(additive_inverse)
#Create a set which only contains unique sqaures from a given a integer list.
integer=[2,3,-4,5,-9,9,-1,-2,-5,8,-6]
sq_set = {i*i for i in integer}
print(sq_set)
    