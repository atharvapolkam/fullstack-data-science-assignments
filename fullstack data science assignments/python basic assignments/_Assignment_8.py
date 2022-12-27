#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Is the Python Standard Library included with PyInputPlus');get_ipython().run_line_magic('pinfo', 'PyInputPlus')
PyInputPlus is not a part of the Python Standard Library, we must install it separately using Pip.


# In[ ]:


get_ipython().set_next_input('Why is PyInputPlus commonly imported with import pyinputplus as pypi');get_ipython().run_line_magic('pinfo', 'pypi')
 pypi is alias of PyInputPlus.
The as pyip code in the import statement saves us
from typing pyinputplus each time we want to
call a PyInputPlus function. Instead we can use
the shorter pyip name


# In[1]:


get_ipython().system('pip install pyinputplus')


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()? 
inputInt() : Accepts an integer value, and returns int value
inputFloat() : Accepts integer/floating point value and returns float value
  


# In[ ]:


import pyinputplus as pyip
pyip.inputInt()
pyip.inputFloat()


# In[ ]:


4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?



# In[ ]:


import pyinputplus as pyip
pyip.inputInt(min = 0, max =99)


# In[ ]:


get_ipython().set_next_input('5. What is transferred to the keyword arguments allowRegexes and blockRegexes');get_ipython().run_line_magic('pinfo', 'blockRegexes')


# In[ ]:


We can also use regular expressions to specify whether an input is allowed or not. 
The allowRegexes and blockRegexes
keyword arguments take a list of regular expression strings 
to determine what the PyInputPlus function will accept or reject as valid input.


# In[ ]:


response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])


# In[ ]:


get_ipython().set_next_input('Q. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')
Ans. It will throw RetryLimitException exception.


# In[ ]:


get_ipython().set_next_input("Q. If blank input is entered three times, what does inputStr(limit=3, default='hello') do");get_ipython().run_line_magic('pinfo', 'do')
When you use limit keyword arguments and also pass a default keyword argument, 
the function returns the default value instead of raising an exception


# In[ ]:


import pyinputplus as pyip
response = pyip.inputStr(limit=3,default='hello')
response


# In[ ]:




