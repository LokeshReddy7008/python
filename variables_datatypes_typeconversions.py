#print("this is my first program")

# hemanth=20
# print(hemanth)

# a=b=c=120
# print(a,b,c)

# a,b,c=2,4,5
# print(a,b,c)

#variable rules 
#good
# lokesh=140
# _lokesh=230

'''variable types'''
# 1.camelCase
#    lokeshReddy=1
# 2.snake_case
#    lokesh_reddy=2
# 3.PascalCase
#    LokeshReddy=3

'''datatypes'''
#a=12 int
# b=23.5 float
# c=True bool
# d=2+4j complex
# to know the type of datatype
#print(type(a))

#Type conversions 
'''1.Implicit  --> No data loss'''
# a=140
# print(float(a))
'''2.Explicit --> Data loss'''
# a=132.54673
# print(int(a))

# to take input
#a=input("enter the value")
#print(a)

''' 
Task 1 - Practice comments, variables, datatypes, input funcions
task 2 - program on simple intrest and compound intrest
task 3 - program on (a+b)**2 
'''

#task 2
#simple_intrest
'''principle_amount=2054
rateofintrest=2
time=12
simple_intrest=(principle_amount*rateofintrest*time)/100
print(simple_intrest)'''

#compount_intrest

''' p=2054
r=2
n=4
t=15
ci=p*(1+r/n)**t
print(ci) '''

# task 3
#program for (a+b)**2
'''a=4
b=6
c=a**2+b**2+(2*a*b)
print(c)'''

a=int(input("enter a value"))
b=int(input("enter b value"))
c=(a)**2+(b)**2+(2*a*b)
print(c)