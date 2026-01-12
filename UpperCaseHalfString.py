#Convert half of a string to uppercase
s = "This is the String to be converted"
#using slicing
half_index = len(s) // 2 #slices the string in half
#python strings are 0 indexed, meaning to get the last character you need index len(s) - 1
result = s[:half_index].upper() + s[half_index:]
print(result)

#using a loop
result2 = ""
for i in range(len(s)): #ie. range(5) - 0, 1, 2, 3, 4, 5
    if i < half_index:
        result2 += s[i].upper()
    else:
        result2 += s[i]
print(result2)


#using list comprehension
result3 = []
for i in range(len(s)):
    if i < half_index:
        result3.append(s[i].upper())
    else:
        result3.append(s[i])
final_result = ''.join(result3) #'' is the place for the separator- what goes in between every character in the list
print(final_result)
