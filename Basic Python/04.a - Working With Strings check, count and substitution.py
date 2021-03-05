

julesQuote = "Well, there's this passage I've got memorized that sort of fits this occasion"


# they will return a boolean
contains = "memorized" in julesQuote
dont_contain = "read" in julesQuote

print(contains)
print(dont_contain)

#rememberthat to be more precise when searching for words in a string,use
# .uppper () or .lower ()

# Counting

angryQuote= "Say 'what' again. Say 'what' again, I dare you, I double dare you motherfucker, say what one more Goddamn time! "

print("The word 'what' appears {} times in this sentence".format(angryQuote.count("what")))
# sadly he said "what"
print("The letter 'a' appears {} times in this sentence".format(angryQuote.count("a")))

# Substitution

vincentQuote = "Now, if you'll excuse me, I'm going to go home and have a heart attack."

newVincentQuote = vincentQuote.replace("a heart attack.", "a sandwich")

print(newVincentQuote)