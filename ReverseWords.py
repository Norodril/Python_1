s = "python is fun"
words_split = s.split()
reversed_words = words_split[::-1]
result = ' '.join(reversed_words) #separator.join(list of strings)
print(result)

#using a loop
for word in reversed(words_split):
    result = result + word + " "

result = result.strip()
print(result) #removes extra spaces at the start and end

