'''

## Lista 

Key attributes
1. Ordered
2. Mutable 
3. can contain any arbitrary objects
4. elements can be accessed by index.
5. Accept duplicated values


'''

# Create a empty list 

L = []

lista = [32,45,56,76]

print(type(lista))
print(lista[0])
print(lista[3])

# convert a string to a list 
print("Converting lists and string\n")
toList = "It will be converted\n"

listaFrase = list(toList)

print(listaFrase)

# convert a list to a string 

toString = "".join(listaFrase)

print(toString)

#  Copying a list
print("Copying lists\n")

## Wrong way"
l1 = [1,2,3,4,5]
l2 = l1 

l2[0] = 100
print("Wrong way")
print(l1) # changed both lists
print(l2)

# Right way

lc1 = [1,2,3,4,5]
lc2 = lc1[:]

lc2[0] = 999

print("Right way")
print(lc1)
print(lc2) # only changed the second list
