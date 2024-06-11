#control statements
'''if 2>3:
    print("this is if")
elif 2>5:
    print("this is elif")
elif 4<3:
    print("this is elif")
else :
    print("this is else")'''

# nested if  ( if within if )
'''if 2>1:
    print("this is outer if")
    if 4>6:
        print("this is inner if")
    else:
        print("this is inner else")
else:
    print("this is outer else")'''

#short Hand-if
'''a=8
b=6
if a>b:print("this is shorthand-if")'''

#short Hand-if else
'''a=9
b=7
print("This is true")if a>b else print("This is false")'''

#Looping ststements
# while loop

# while True:
#     print("this is loop")
    
'''lokesh=20
while lokesh<=25:
    print("This is lokesh",lokesh)
    lokesh+=1
else:
    print("This is not lokesh")'''

#for loop
'''for i in "lokesh":
    print(i)
for i in range(0,10,3):
    print(i)'''

#break statement
'''for i in "lokesh":
    if(i=="e"):
        break
    print(i)'''

#continue statement
'''for i in "lokesh":
    if(i=="e"):
        continue
    print(i)'''

# Task 7
''' Practice operators, conditional statements, looping statements, transfer statements'''
# Task 8
''' prepare Docs on your topics'''
# task 9
''' explore stack overflow (website that helps to rectify errors)'''

n=10
for i in range(n):
    result=0
    result=result+i
    print(result)