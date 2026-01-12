from itertools import compress
#print only the words whose length is even
#list compression
sentence = "This is the String"
#split() splits the string on any whitespaces 
List = sentence.split() #now a list
even = []
for word in List:
    if len(word) % 2 == 0: 
        even.append(word)
result = " ".join(even)
print(result)

#using list comprehension
#expression for item in iterable if condition
#expression = what you want to put in the list
#item for item in iterable = loop through each item
# if condition - only include the item if condition is met
even_words = (w for w in List if len(w) % 2 == 0)
result2 = " ".join(even_words)
print(result2)

#using itertools
selectors = []
for w in List:
    if len(w) % 2 == 0:
        selectors.append(True)
    else:
        selectors.append(False)
result3 = " ".join(compress(List, selectors)) #compress(data, selectors) returns elements from the data where the corresponding element in selectors is True
print(result3)
