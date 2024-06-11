# # tuple 
# # tuples are immutuable

# # loki=(1,23,"lok",48.9)
# # print(type(loki))
# # print(loki[0])


# # tuple operations
# a1=(1,2,3)
# a2=(4,5,6)
# print(a1+a2)       # concatenation
# print(a2*4)        # Repetition
# s=zip(a1,a2)
# print(tuple(s))    # assigns o index value in one variable to another zero index value
# print(2 in a1)     # membership
# print(5 not in a1) # membership
# print(a1 is a2)    # to check whether t1 is same in t2
# print(a1 is not a2)


# # loop in tuple
# l=(36,47,825,7353,634)
# for i in l:
#     print(i)


# bank problem

a=''' 
      1. Debit
      2. Credit
      3. Mini Statement
      4. Exit
'''

name="lokeshreddy"
passwords="7008"
user_name=input("Enter the user name : ")
password=input("Enter the Password : ")
amount=1000
if user_name==name and password==passwords:
    while True:
        print(a)
        option=int(input("Enter your option :"))
        if option==1:
            debit_amount=float(input("Enter the amount :"))
            amount-=debit_amount
            print("Amount after Debit ",amount)
        elif option==2:
            credit_amount=float(input("Enter the amount :"))
            amount+=credit_amount
            print("Amount after Credit ",amount)
        elif option==3:
            print("Amount ",amount)
        elif option==4:
            break
else:
    print("Incorrect")