#Verify whether a given string has at least one letter (either and at least one number)

#using any
s = "abc123"
#any(iterable) is a built in function that checks whether 
letterCheck = False
for c in s:
    if c.isalpha():
        letterCheck = True
        break

numberCheck = False
for c in s:
    if c.isdigit():
        numberCheck = True
        break

if letterCheck and numberCheck:
    print("True")
else:
    print("False")



#Using for loop
for char in s:
    if char.isalpha():
        letterCheck = True
    if char.isdigit():
        numberCheck = True
    if letterCheck and numberCheck:
        print("True")
        break #once we know the answer is True, we stop looping to avoid it from continuing
    else:
        print("False")

#Using built in String Methods like set.isdisjoint()
letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = set("0123456789")
s_set = set(s)
#A.isdisjoint(B) - Do A and B have NO elements in common?
if s_set.isdisjoint(letters) == False and s_set.isdisjoint(numbers) == False:
    print("True")
else:
    print("False")