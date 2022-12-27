#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
true and false represent as 1 and 0 respectively


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
AND, OR, NOT


# In[ ]:





# In[ ]:


3. Make a list of each Boolean operator 39;s truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate .
                NOT      AND     OR                                          
false	false	true	false	false
false	true	true	false	true
true	false	false	false	true
true	true	false	true	true
                                                           


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
a)false
b)false
c)true
d)false
e)true


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
less than ( < ), less than or equal to ( <= ), greater than ( > ),
greater than or equal to ( >= ), equal to ( == ), and not equal to ( != )


# In[1]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
we denote '=' for assignment operator
and == for equal to
when we want to assign some value to a variable then we use =
and == for represent conditions


# In[2]:


7. Identify the three blocks in this code:
spam = 0
if spam ==10;
print('eggs')
if spam > 5 :
    print('bacon')


# In[5]:


spam = 0
if spam ==10:
    print('eggs')
if spam > 5 :
        print('bacon')
else :
        print('ham')
        print('spam')
        print('spam')
    
   
   


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[8]:


spam=0
if spam==1:
    print('hello')
if spam==2:
    print('howdy')
else :
    print('Greetings!')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
interupt the kernal


# In[9]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
the main difference is between both the statements  that when break keyword comes,
it terminates the execution of the current loop
and passes the control over the next loop or main body,
whereas when continue keyword is encountered, it skips
the current iteration and executes the very next iteration in the loop


# In[ ]:


In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[24]:


a=range(0,10)
b= range(0,10,1)


# In[25]:


list(a)


# In[26]:


list(b)


# In[ ]:


there is no such diffrence in output but we denote 1 as


# In[ ]:


Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[61]:


a=1
while a<11:
     print(a)
     a=a+1
   
   
    
   


# In[54]:



for x in range(1,11):
    print(x)
    


# In[56]:


i = 1
while i < 6:
    print(i)
    i += 1
    
  


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')


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




