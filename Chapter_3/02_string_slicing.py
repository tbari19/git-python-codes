greeting = "Good Morning, "  
name = "tushar"
print(type(name))      # to know type of name variable

# Concatenating two strings
c = greeting + name    
print(c)

name = "lokesh"
print(name[4])

# name[3] = "d" --> Does not work

print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

name = "JayShriRam"
d = name[0::3]   #skip value of 2--> format start:end:skip value 
e = name[:0:-1]  # print reverse string 
print(d)
print(e)