#List

#lokesh=[]
#print(type(lokesh))

'''lokesh=[1,45.6,"loki",True]   # method 1
lokesh2=list([1,87.8,"loke"]) # method 2 ( we use this method when we wanr to do typr conversions )
print(lokesh)
print(lokesh2)'''

#index in list (index always starts with "0" and ends with "n-1")
'''reddy=[7,87.6,764,"loki"]
print(reddy[3])'''

#slicing in list
'''loki=[5,67,796,'true',76,34]
print(loki[0:5:4]) # [start:stop:skip]
print(loki[2:])
print(loki[::])   # prints all data
print(loki[::-1]) # list reverse
loki[1]="reddy"   # replace data 
print(loki)'''

# List Methods

'''list=[2,5,8,99,65,76,34,24,2,76,2]'''
'''list.append(143)'''        # adda data to last in list
'''list.extend([143])'''      # add data to last but [] compulsory
'''a=list.copy()'''           # copy the list to another variable
'''print(a)'''                
'''list.clear()'''            # clear the list
'''print(list.count(2))'''    # finding count of the element
'''print(list.index(99))'''   # finding index value
'''list.insert(2,108)'''      # insert data into list  by its index values
'''list.pop(0)'''             # removes data based on index values
'''list.remove(65)'''         # removes the data called 65 in list
'''list.reverse()'''          # reverse the list
'''list.sort()'''             # prints in ascending order
'''list.sort(reverse=True)''' # prints descending order
# print(list)

# List compherension

'''list=["even" if i%2==0 else "odd"  for i in range(10)]
 print(list)'''

'''list=["apple", "guava", "lokesh", "tomato", "egg"]
new_list=[i for i in list if "a" in i]
print(new_list)'''

# finding index values for repeating values
l=[1,2,2,3,4,5,1]
for i in range(len(l)):
    if l[i]==1:
        print(i)

# removing repeated all elements at one time
'''list=[1,2,3,3,3,4,2,3,4,3,3,3,8,6,9]
n=[]
for i in list:
    if i==3:
        list.remove(3)
    else:
        n.append(i)
print(n)''' 


# Task 10
'''Practice List, List methods, List comprehensions'''
# Task 11
'''prepare docx on list'''
# Task 12
'''explore jira'''
