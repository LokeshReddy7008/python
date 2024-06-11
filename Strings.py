# Strings and methods in python
#a='lokesh'       # method 1 to declare a string
#b="lokesh"       # method 2 to declare a string
#c='''lokesh'''   # method 3 to declare a string

a="lokesh"
print(a.upper())      # to change into uppercase
print(a.lower())      # to change into lowercase
print(a.isalpha())    # to check whether given string is alphabets or not
print(a.isnumeric())  # to check whether given string is numeric or not
print(a.isalnum())    # to check whether given string is either alphabets or numeric


b="i am lokesh my name is lokesh"
print(b.count("lokesh"))          # used to count how many times word present
print(b.index("is"))              # used to find index value
print(b.find("is"))               # used to find index value
print(b.startswith("am"))         # used to check whether given string starts with am
print(b.endswith("h"))            # used to check whether given string ends with h

# strip ( trims or cuts)
d=" this is python  "
print(len(d))
s=d.strip()         # used to remove empty spaces
print(len(s))
s=d.lstrip()        # used to remove left side empty spaces
print(len(s))
s=d.rstrip()        # used to remove right side empty spaces
print(len(s))

name="na book na istam"
print(name.title())     # change every word starts with capital letter
r=name.replace("book","note").replace("istam","wish")    # used to replace one word with another 
print(r)

new="i am learning python"
print(new)
f=new.split()   # converts string into list 
print(f)
j=" ".join(f)
print(j)

# format
c="hello {} how are you, this is {}".format("lokesh","reddy")
print(c)

# using loop to print more names at a time
names=["lokesh","reddy","ram","ramesh","krish"]
for i in names:
    print("this is {}".format(i))











# program to store strings ends with in
list=["abc.com","xyz.in","w3schools.in"]
new_list=[]
for i in list:
    if i.endswith("in"):
        new_list.append(i)
print(new_list)