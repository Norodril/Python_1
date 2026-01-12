#method 1: Using len() function
a = "Hello, World"
print(len(a)) 

#using a loop and in operator
count = 0
for char in a:
    count += 1
print(count)

#using enumerate()
l = 0
for i, ch in enumerate(a):
    l += 1 #adds 1 for each character
print(l)

#using str.count()
length = a.count("") - 1
#python defines the empty string as being between each character including before the first and after the last
#thus, for hello, it will count length + 1, so a.count("") - 1 will give us the length of a
print(length)