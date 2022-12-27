#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[ ]:


a=float(input("enter a distance in km"))
b=a*0.621
print('conversion in miles:',b)


# In[ ]:


get_ipython().set_next_input('2. Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[ ]:


a=float(input("enter a temperature in celcius:"))
b=(a*9/5)+32
print('conversion in fahrenheit is:',b)


# In[9]:


def conversiontofahrenheit():
    a=float(input("enter a temperature in celcius:"))
    b=(a*9/5)+32
    print('conversion of degree celcius to fahrenheit is:',b)
conversiontofahrenheit()
    
    





# In[4]:


def celtofahr():
    a=float(input("enter temp in celcius"))
    b=(a*9/5)+32
    print("{} degree celcius to {}fahrenheit".format(a,b))
celtofahr()
    


# In[3]:


celtofahr(20)


# In[10]:


celtofahr()


# In[ ]:


get_ipython().set_next_input('3. Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[29]:


import calendar

def calendar1():
    a=int(input("enter year of calendar:"))
    print (calendar.calendar(year))
calendar1()
    
        


# In[23]:


import calendar

def showCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
showCalender()


# In[ ]:


4.Write a Python program to solve quadartic equation ?


# In[2]:


import cmath
import math

def quadarticEquationRoots(a,b,c):
    
    discriminant = b*b-4*a*c
    
    if discriminant == 0:
        r1 = -b/2*a
        r2 = -b/2*a
        print("Roots are Real",r1,r2)
    elif discriminant > 0:
        r1 = (-b-math.sqrt(discriminant))/(2 * a)
        r2 = (-b+math.sqrt(discriminant))/(2 * a)
        print("Roots are Real and different",r1,r2)
    else:
        r1 = (-b-cmath.sqrt(discriminant))/(2 * a)
        r2 = (-b+cmath.sqrt(discriminant))/(2 * a)
        print("Roots are Imaginary",r1,r2)


a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

quadarticEquationRoots(a,b,c)


# In[ ]:


5.Write a Python program to swap two variables without temp variable ?


# In[1]:


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


def swapNumbers(num_1,num_2):
        print('Before Swapping',num_1,num_2)
        num_1 = num_1+num_2
        num_2 = num_1-num_2
        num_1 = num_1-num_2
        print('before Swapping',num_1,num_2)

swapNumbers(num_1,num_2)


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




