#A string is given, and you have to find all words greater than length k

#definiting a function
def string_k(k, t): 
    strings = [] #empty list to store result
    text = t.split(" ") #stores the string in a list split by words
    for x in text: #for word in the 'text' list
        if len(x) > k: #if the length of the word > k
            strings.append(x) #add it to the list
    return strings

k = 3
strings = "This is the string"
print(string_k(k, strings))

#using list comprehension
length = k
result = []
words = strings.split()
for word in words:
    if len(word) > length:
        result.append(word)
print(result)

#using enumerate
result2 = []
for i, a in enumerate(words): #enumerate lops over something and gives you both the index and the value
    #for index, element in enumerate
    if len(a) > length: #length of the elemnt > length
        result2.append(a)
print(result2)