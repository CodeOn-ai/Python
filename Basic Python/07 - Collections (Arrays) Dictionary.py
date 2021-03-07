# Every dictionary has a key and a corresponding value, key and value is made between {}

# list = []; tuple = (); dict = {key:value}

'''
Dictionary

1. Not Ordered
2. Mutable
3. Don't accept duplicated values
'''

firstDict = {
    "Brand": "Ford",
    "Doors": 4,
    "Year": 2021
}

print(firstDict)
print(firstDict.keys())
print(firstDict.values())

# Don't accept duplicated values
firstDict = {
    "Brand":"Ford",
    "Doors":2, # will be ignored /overwrited
    "Doors":4,
    "Year":2021
}

print(firstDict)
print(len(firstDict))
print(type(firstDict))


# check key values,

brand = firstDict ["Brand"]
print(brand)
# or
print(firstDict.get ("Brand"))

# Check items

checkItems = firstDict.items()
print(checkItems)