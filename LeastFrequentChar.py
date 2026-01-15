from collections import Counter

#Given a string, Identify the character than appears the least number of tiems

#using collections.Counter
s = "TThhiiss iiss tthhe SSttrriinngg"
frequency = Counter(s.lower()) #Counts how many times each element appears in an iterable
#key is the letter values is the count
result = min(frequency, key = frequency.get)
#min(iterable, key = function)- min() iterates over the keys in frequency, and for each key, it calls 
#frequency.get(key) that takes a key as input and returns the value associated with that key in the dictionary
print(result)

#Using Dictionary
dictionary = {}
for char in s.lower():
    dictionary[char] = dictionary.get(char, 0) + 1 #dictionary.get(char, 0) checks if the key char exists in the dictionary
    #if it exists, it returns its value; if it does not exist, it returns 0 + 1 - frequency count
result2 = min(dictionary, key = dictionary.get) #key = dictionary.get returns the value for that given key
print(result2)
