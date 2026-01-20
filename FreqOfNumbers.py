import re
#Given a string we determine how many digits are in the string
String = "This is the String with 1234 digits"

#using re.findall(pattern, string) finds all matches of a pattern in a string and returns as a list
result = len(re.findall(r'\d', String))
print(result)

#using sum() and findall()
result2 = 0
for match in re.findall(r'\d', String):
    result2 += 1
print(result2)

#Using map
result3 = sum(map(str.isdigit, String)) #sum for booleans = True behaves like a 1 false behaves like a 0
#map applies a function to each item in an iterable - map(function, iterable)
print(result3)

#using isdigit()
result4 = 0
for char in String:
    if char.isdigit(): #returns a true if the character is a digit
        result4 += 1
print(result4)

#using loops()
result5 = 0
digits = '0123456789'
for char in String:
    if char in digits:
        result5 += 1
print(result5)