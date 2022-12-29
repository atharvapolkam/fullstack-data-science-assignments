#!/usr/bin/env python
# coding: utf-8

# In[32]:


get_ipython().set_next_input('1. Write a Python Program to Find the Factorial of a Number');get_ipython().run_line_magic('pinfo', 'Number')
    

    


# In[33]:


i=int(input("enter a number:"))
fact=1
while i>0:
    fact=fact*i
    i=i-1
print("factorial=",fact)
        


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')


# In[23]:


table=int(input("enter a number:"))
start=int(input("start for the table:"))
end=int(input("end for that table:"))
while (start<=end):
    print(start,"*",table,"=",start*table)
    start=start+1


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')


# In[25]:


num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[29]:


number = int(input("enter a number:"))
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num/10
  sum += pow(digit,length)
if sum==number:
  print("Armstrong")
else:
  print("Not Armstrong")


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')


# In[31]:


# Program to check Armstrong numbers in a certain interval

lower = int(input("enter lower ranger:"))
upper = int(input("enter upper ranger:"))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[ ]:


get_ipython().set_next_input('6. Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# In[34]:


num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




