#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What is the result of the code, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, b=6, c=8):

print(a, b, c)

func(1, 2)


# In[1]:


def func(a, b=6, c=8):
    print(a, b, c)
func(1, 2)

'''This funtion is taking a positional argument and 2 keyword argument. When function call m=is made, parameter passed are a=1,b=2. When the function is executed , parameter c=8 will be taken by default as its a keyword argument.
    solution is = 1,2,8'''


# In[ ]:


get_ipython().set_next_input('2. What is the result of this code, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, b, c=5):

print(a, b, c)

func(1, c=3, b=2)


# In[6]:


def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)

''' The result of the above code is 1 2 3.It is because the function will use default values only when a value for a argument is not provided and if the argument name is mentioned while doing a function call, the order of arguments is also ignored by the python interpreter'''


# In[ ]:


get_ipython().set_next_input('3. How about this code: what is its result, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, *pargs):

print(a, pargs)

func(1, 2, 3)


# In[5]:


def func(a,**kargs):
    print(a,kargs)
func(a=1,c=3,b=2)

'''The result of the code is 1 (2,3). *pargs stands for variable length arguments. This format is used when we are not sure about the number of arguments to be passed to a function. All the values under this argument will be stored in a tuple.'''


# In[ ]:


get_ipython().set_next_input('4. What does this code print, and why');get_ipython().run_line_magic('pinfo', 'why')
def func(a, **kargs):

print(a, kargs)

func(a=1, c=3, b=2)


# In[7]:


def func(a,**kargs):
    print(a,kargs)
func(a=1,c=3,b=2)

'''The result of the above code is 1 {'c': 3, 'b': 2}. **kargs stands for variable length keyword arguments. This format is used when we want pass key value pairs as input to a function. All these key value pairs will be stored in a dictionary'''


# In[ ]:


get_ipython().set_next_input('5. What gets printed by this, and explain');get_ipython().run_line_magic('pinfo', 'explain')
def func(a, b, c=8, d=5): print(a, b, c, d)

func(1, *(5, 6))


# In[8]:


def func(a,b,c=8,d=5):
    print(a,b,c,d)
func(1,*(5,6))
'''The output of the above is 1 5 6 5. The reason for this function not throwing an error is because, this function expects 4 arguments. The value for a is provided explicitly whereas for arguments b and c, the function will expand *(5,6) and consider the value of b as 5 and value of c as 6. Since the default value of d is provided in function declaration, d value will be 5. However it is recommended to use the feature of positional arguments at the end.'''


# In[ ]:


get_ipython().set_next_input('6. what is the result of this, and explain');get_ipython().run_line_magic('pinfo', 'explain')
def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'

l=1; m=[1]; n={'a':0}

func(l, m, n)

l, m, n


# In[ ]:


def func(a, b, c): 
    a = 2; b[0] = 'x'; c['a'] = 'y'
    
l=1; m=[1]; n={'a':0}
func(l, m, n)

l, m, n


# In[ ]:


(1, ['x'], {'a': 'y'})


# In[9]:


'''Here in the code, the list and dict are passed as argument, and those are mutable. Here the list l and parameter b point to the same list in the memory location where as dict n and c point to the same memory location. Any updates to this list will update in the memory locationl = 1 , integer values, immutable, m is list, mutable, n is dict, mutable. output will be = 1,['x'],{'a':'y'}'''


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




