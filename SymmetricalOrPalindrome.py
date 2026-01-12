#Symmetrical if the first half matches the second half, ingoring the middle character if odd
#Palindrome if it reads the same forwards and backwards
#best method for this is using string slicing
#directly compares parts of the string
s = "abaaba"
half = len(s) // 2 #floor division; always rounds down
#checks whether the string is even or odd length
#returns True or False in a variable sym
if len(s) % 2 == 0:
    sym = s[: half] == s[half: ]
else:
    sym = s[:half] == s[half + 1:] #skip the middle char

if sym: 
    print(f"{s} is symmetrical")
else:
    print("Not symmetrical")

#start, stop, step
pal = s == s[::-1] #reverses the string and checks if equal

if pal: print (f"{s} is a palindrome")
else: print ("Not a palindrome")