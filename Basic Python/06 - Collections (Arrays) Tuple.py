"""
## Tuple

1. Ordered
2. Immutable
3. Accept duplicated values
"""

# list uses [], tuple ()

sTuple = ("banana", "apple", "strawberry")
print (sTuple)

# size of a tuple is done in the same way as list

print(len(sTuple))

# Creating a tuple with an element

cTuple = ("tomato",)

will_it_be_Tuple = ("tomato") #?

print (type(cTuple))
print (type(will_it_be_Tuple))

# update a tuple

aTuple = (2, "b", "d")

print(aTuple)

# convert tuple to list
listTuple = list (aTuple)
listTuple [0] = "a"

# convert list back to tuple
aTuple = tuple (listTuple)

print (aTuple)
print (type (aTuple))

# as tuple cannot be changed, converting to list is a common technique for
# to apply


# packing = assign value to the elements of a tuple

zTuple = ("Banana", "Avocado", "Strawberry")

(yellow, green, red) = zTuple

print (yellow)
print (green)
print (red)


print ("To use to create a list using packing")

wTuple = ("Banana", "Avocado", "Strawberry", "Apple")

(yellow, green, * red) = wTuple 

print (yellow)
print (green)
print (red)