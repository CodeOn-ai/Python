# String is a type of data that is focused directly on the human side,
# for easy reading

movie = "Pulp Fiction"

print(movie)
print(type(movie))

# To access a value in a string we use its index, this is represented
# by [index] in front of the variable Note: in most programming languages
# the first element always has the first index / index 0

print(movie[0])
print(movie[1])
print(movie[2])
print(movie[3])
print(movie[4])
print(movie[5])
print(movie[6])
print(movie[7])
print(movie[8])
print(movie[9])
print(movie[10])
print(movie[11])

# Important to note that even space counts as an element in a string

# Verify the string

fullname = "Jules Winnfield"
print(fullname.startswith("Jules"))
print(fullname.endswith("Winnfield"))

# python is "case sensitive" 
print(fullname.startswith("jules"))

# to normalize it use lower function
print(fullname.lower().startswith("jules"))
