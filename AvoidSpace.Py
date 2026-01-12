import re
s = "Hello how are you"
#using replace
print(len(s.replace(" ", ""))) #prints the number of characters not including spaces

#using a for loop
res = 0
for char in s:
    if char != " ":
        res += 1
print(res)

res = len(re.sub(r" ", "", s))
print(res)
#regex is a pattern language used for searching and manipulating strings
#it is a way to search, match, and modify text using rules
#re.sub(pattern, replacement, string) replaces occurrences of the pattern in the string with the replacement
res = len(re.sub(r" ", "", s)) #r is used for safety and consistency in this case- there is no backslash
print(res)
