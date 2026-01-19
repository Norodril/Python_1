from collections import Counter
from collections import defaultdict

#Finding Characters with odd frequencies in a string 
#Involves identifying which characters appear an odd number of times
#Output will be a list of characters with odd frequencies

s = "This is the String"

#Using Counter
frequency = Counter(s)
result = []
for char, count in frequency.items():
    if count % 2 != 0:
        result.append(char)
print(result)

#Using Defaultdict
frequency = defaultdict(int) #default value for each key is 0
for char in s:
    frequency[char] += 1

result2 = []
for char, count in frequency.items(): #we want to loop over both the keys and the values
    if count % 2 != 0:
        result2.append(char)
print(result2)


#Using List Comprehension
result3 = []
for char in set(s):
    if s.count(char) % 2 != 0:
        result3.append(char)
print(result3)

#Using Loop and Dictionary
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1 #dictionary with the counter
    else:
        frequency[char] = 1 #if it hadn't appeared before, initialize count to 1

result4 = [] #creates a list
for ch, count in frequency.items(): #frequency.items() gives you pairs of data from the dictionary as a tuple
    if count % 2 != 0: #if the count is odd
        result4.append(ch)
print(result4)

