#check if a String contains any special character
#Using Regular expression

String = "This$Is%The(String)"

#using regular for loop iteration
String.split() 
count = 0
Chars = '[@_!#$^&*()<>?/\|}{~:}]'
for i in range(len(String)): #range creates a sequence from 0 until the end of whatever number it is fed
    if String[i] in Chars:
        count += 1

if count > 0:
    print("Special Char Exists")
else:
    print("Special Char does not exist")

#defining a function
def has_special_char(String):
    for char in String:
        if not (char.isalpha() or char.isdigit() or char == ' '):
            return True
    return False

if has_special_char(String):
    print("The string contains special characters.")
else:
    print("The String does not contain special characters.")

#using string.punctuation
import string
def check_string(s):
    for char in s:
        if char in string.punctuation:
            print("String contains special char")
            return
    print("String does not contain special char")

check_string("Hello$World")
check_string("Hello World")