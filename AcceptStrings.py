#returns true if a given string contains a vowel
#returns false if the given string does not contain a vowel

#using set()
vowels = "this is the string"
no_vowels = "nw qrty"

vowel_set = set("aeiouAEIOU")
if set(vowels.lower()) & vowel_set: #if the set is not empty (intersection of any kind), it will evaluate to true
    print("True")
else: 
    print("False")

if set(no_vowels.lower()) & vowel_set: #if there is an intersection of any kind between the elements of both sets
    print("True")
else: 
    print("False")

#using all()
for letter in vowels:
    if letter.lower() in vowel_set:
        print("True")
        break
else:
    print("False")

for letter in no_vowels:
    if letter.lower() in vowel_set:
        print("True")
        break
else:
    print("False")

#using a for loop through the string
for char in vowels.lower():
    if char in vowel_set:
        print("True")
        break
else:
    print("False")

for char in no_vowels.lower():
    if char in vowel_set:
        print("True")
        break
else:
    print("False")