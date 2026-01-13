#count the number of vowels in a given string

#using for loop()
s = "This is an example string"
vowels = "aeiouAEIOU"
vowels_set = set(vowels)
count = 0
for char in s:
    if char in vowels_set:
        count += 1

print(count)

#using casefold()
vowels2 = "aeiou"
s_lower = s.casefold() #similar to lower(), but more aggressive
#generator expression syntax - <expression> for <variables> in <iterable> if <condition>
count2 = sum(1 for char in s_lower if char in vowels2)
print(count2) #every time char is in s_lower and vowels2, it returns 1 and is then summed

#Using count()
count3 = sum(s_lower.count(char) for char in (set(s_lower) & vowels_set)) #s_lower.count(char) goes through the entire string s_lower and returns how many times char appears in both s_lower and vowels_set
print(count3)

