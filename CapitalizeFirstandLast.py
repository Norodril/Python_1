#using List Comprehension
s = "This is the String"
split = s.split() #returns a list with each word as an element
processed_words = []
for i in split:
    if len(i) > 1:
        first_letter = i[0].upper()
        middle_letters = i[1:-1]
        last_letter = i[len(i) - 1].upper()

        new_word = first_letter + middle_letters + last_letter
    elif len(i) == 1:
        new_word = i.upper()
    else:
        print("Error: Empty String")
    processed_words.append(new_word)

result = " ".join(processed_words)
print(result)

#using map()
#map function is used to apply a function to every item of an iterable and return a new iterable w/that result
#map(function, iterable)
