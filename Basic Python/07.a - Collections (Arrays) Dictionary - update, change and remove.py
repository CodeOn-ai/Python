# changing values ​​and updating

firstDict = {
    "Brand": "Ford",
    "Doors": 4,
    "Year": 2021
}


firstDict ["Year"] = 2018

print (firstDict)

update = firstDict.update({"Year of purchase": 2019})

print (firstDict)

# to remove an item

removed = firstDict.pop("Year of purchase")

print (firstDict)

# deleting item

secondDict = {
  "brand": "Chevrolet",
  "model": "Monza",
  "year": 1983
}
del secondDict ["model"]
print (secondDict)

# emptying dictionary

secondDict.clear()
print (secondDict)

# copying dict
maisDict = {
  "brand": "Chevrolet",
  "model": "Monza",
  "year": 1983
}

anotherDict = maisDict.copy ()

print (anotherDict)