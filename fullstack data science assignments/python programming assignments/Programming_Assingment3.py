#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Check if a Number is Positive, Negative or Zero');get_ipython().run_line_magic('pinfo', 'Zero')


# In[ ]:


a=float(input('enter a no:'))
if a == 0:
    print("given number is a zero")
elif a > 0 :
        print("given number is positive")
else :
            print("given no is negative")


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Check if a Number is Odd or Even');get_ipython().run_line_magic('pinfo', 'Even')


# In[ ]:


def checknum(num):
    
    if num%2==0:
        print('{} is a even number'.format(num))
    else:
        print('{} is a odd number'.format(num))
num= int(input("enter a no:"))

checknum(num)
   

    


# In[ ]:


checknum(7)


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')


# In[ ]:


def checkyear(year):
    if year%4 ==0:
         print('{} is a leap year'.format(year))
    else :
        print('{} is not a leap year'.format(year))
        
   
year = int(input('enter a year:'))
checkyear(year)

    


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[ ]:


num=int(input("enter a no:"))
for i in range(2,num):
    if num% i ==0:
        print('prime')
        break
        
    else:
        print('not prime')
        break


# In[ ]:


5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[4]:


l=int(input("beginning of interval:"))
u=int(input("end of an interval"))

for num in range(l,u+1):
    if num > 1:
        for i in range (2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




