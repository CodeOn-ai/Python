# Slicing 

# L = [index 0,index 1, index 2, index 3]
L = [3,4,5,6]

print(L[0:2])

# Notices that when slicing a list, the first index is included while
# the last one is not (index 0 = 3 and index 2 = 5)

# to slice the list from right to left, use the negative value

# note that the first index from right to left is 1 and not 0, however
# when slicing the list the last index is excluded (in this case the 6 because 
# it is -1)
print (L [-4: -1])

# to include the last element, leave the right side to do

print (L [-4:])

# check the size of a list 
l = [2,3,4,5,6,7,7,8]

size_list = len(l)
print(size_list)

# add an element to a list

l.append (4) # the new element will be added to the end of the list
size_list = len(l)
print(size_list)

# Remove

L = ["a", "b", "c"] 

del L[1]

print(L)

# Using range to create a list

L = list(range(101))

del L[1:99]

print(L)