from collections import OrderedDict
#Remove all duplicate chars from a string while keeping the first occurence of each character in its original order

#using dict.fromkeys()
s = "This is the String"
result = "".join(dict.fromkeys(s)) #each character becomes a key; values = none
#"".join() concatenates the keys into a single string
#dictionary = collection of UNIQUE keys w/value pairs, so when turning the chars of a string into a dictionary,
#python runs through and checks if the char is already a key, returning keys w/out duplicates
#.join() concatenates elements of an interable into a string
print(result)

#using OrderedDict.fromkeys()
result2 = "".join(OrderedDict.fromkeys(s)) #OrderedDict.fromkeys(string) creates an OrderedDict with unique keys with automatic values = None
#OrderedDict preserves the order in which keys first appear in s
print(result2)

#Using loop with a set
already_seen = set() #add characters that already exist in the string s
result3 = ""
for char in s:
    if char not in already_seen:
        already_seen.add(char)
        result3 += char
print(result3)
