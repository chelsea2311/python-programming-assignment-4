#!/usr/bin/env python
# coding: utf-8

# PYTHON BASIC PROGRAMMING ASSIGNMENT 4

# Q1. FIND THE FACTORIAL OF THE NUMBER

# In[2]:


num =int(input("Enter a number "))
fact = 1
for i in range(num,0,-1):
    fact=i*fact
print("Factorial of number",num,"is",fact)


# Q2.DISPLAY THE MULTIPLICATION TABLE

# In[3]:


num = int(input("Enter a number: "))
for i in range(1,11):
    print(num ,"x",i,"=",num*i)


# Q3.FIBONNACCI SEQUENCE

# In[4]:


a = 0
b = 1
n = int(input("Enter a number "))
print(a)
print(b)
if n == 0:
    print(0)
elif n < 0 :
    print("Invalid")
else :
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)


# Q4. CHECK AMRSTRONG NUMBER

# In[5]:


n = int(input("Enter a number: "))
c = 0
d=n
o=len(str(n))
while d>0:
    s=d%10
    c=c + (s**o)
    d = d// 10
if n==c:
    print("The number",n,"is an Armstrong number")
else:
    print("The number",n,"is not an Armstrong number")


# Q5 CHECK ARMSTRONG NUMBER IS AN INTERVAL

# In[7]:


lower=int(input("Enter number:"))
upper=int(input("Enter number:"))
for i in range(lower,upper+1):
    o=len(str(i))
    c=0
    d=i
    while d>0:
        s=d%10
        c=c + (s**o)
        d = d// 10
    if i==c:
        print(i)


# Q6. SUM OF NATURAL NUMBER

# In[9]:


n = int(input("Enter a number: "))
a=0
for i in range(1,n+1):
    a=i+a
print(a)


# In[ ]:




