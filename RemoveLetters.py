import re

#using replace()
s = "This is the string" 
s = s.replace("This", "")
print(s)

#using re.sub()
#re.sub can delete instead of replacing when nothing is put in the second spot
s = re.sub("is", "", s)
print(s)


