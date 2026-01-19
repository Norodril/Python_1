from collections import Counter
#Count the frequency of a specific character in a string list in python
#determines how often certain characters appear within a given string

#Using collections.Counter
String_list = ["this is the string"]
char_list = ["t", "s", "i"]
result = {}
counter = Counter("".join(String_list)) #creates a counter from the joined string))
for key, value in counter.items():
    if key in char_list:
        result[key] = value
print(result)

#using dictionary
char_count = {}
for s in String_list: #here, s is the string in the list
    for char in s: #c takes on the value of each character in the string
        if char in char_list:
            char_count[char] = char_count.get(char, 0) + 1 #returns the current count + 1 - works like a counter
print(char_count)

#Using dictionary comprehension

joined_string = "".join(String_list) #joins all strings in the list into one big string
filtered_chars = []
for char in joined_string:
    if char in char_list:
        filtered_chars.append(char)

counted_chars = Counter(filtered_chars)
result3 = {}
for key, value in counted_chars.items():
    result3[key] = value
print(result3)