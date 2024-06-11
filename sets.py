# sets          ( set is unordered and index values doesnt works)
# set doesnt allow duplicate values


lokesh={1,3,454,6}
#print(type(lokesh))

''' Sets Methods '''
lokesh.add(142)               # adds data into set
print(lokesh)
lokesh.update({3,6,76,9,1})   # update more elements
print(lokesh)                 
lokesh.remove(9)              # removes specified data
print(lokesh)
lokesh.pop()                  # either it deletes smallest value from set or random value
print(lokesh)
reddy=lokesh.copy()           # copies to another vaiable
print(reddy)
print(reddy.clear())          # clears the entire data

''' Set operations '''
set1={1,2,3,4,5}
set2={5,6,7,8,9,10,4}
a=set1.union(set2)                  # union helps to add both sets without allowing duplicates
print(a)
b=set1.intersection(set2)           # Intersection prints common element on both sets
print(b)
c=set1.difference(set2)             # common elements from both sets get subtract and prints remaining elements from only set1
print(c)
d=set1.symmetric_difference(set2)   # Opposite to intersection, it prints except intersect values
print(d)
print(set1.isdisjoint(set2))        # checks whether both sets are joint sets or disjoint sets, if elements in both sets are same then it is disjoint

s1={1,2,3}
s2={1,2,3,4}
print(s1.issubset(s2))              # ( subset is child class ) states that all elements of s1 are presented in s2 
print(s1.issuperset(s2))            # ( superset is parent class ) states that all elements of s2 are presented in s1
print(s2.issuperset(s1))            

# frozen set
''' whenever we chnage from a mutuable data to immutable data then it is called frozen set
    Once we change into frozenset we cannot perform any methods or operations etc
    Again we want to do operations on the data we hvae to change the data into any type'''
# example 
l=[1,2,3,4,5]
d=frozenset(l)
print(l)
d.append(2)   # once it converts into frozen set, no more operations was accaptable
print(d)

''' loop in sets '''
for i in {1,2,3,4}:
    if i==2:
        print("yes")
    else:
        print("false")