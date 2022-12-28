#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What is the result of the code, and explain');get_ipython().run_line_magic('pinfo', 'explain')
X = 'iNeuron'

def func():

print(X)

func()


# In[1]:


X = 'iNeuron'
def func():
    print(X)
func()


# In[ ]:


get_ipython().set_next_input('2. What is the result of the code, and explain');get_ipython().run_line_magic('pinfo', 'explain')
X = 'iNeuron'

def func():

X = 'NI!'

func()

print(X)


# In[2]:


X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)


# In[ ]:


get_ipython().set_next_input('3. What does this code print, and why');get_ipython().run_line_magic('pinfo', 'why')
X = 'iNeuron'

def func():

X = 'NI'

print(X)

func()

print(X)


# In[3]:


X = 'iNeuron'
def func():
    X = 'NI!'
    print(X)

func()
print(X)


# In[ ]:


get_ipython().set_next_input('4. What output does this code produce? Why');get_ipython().run_line_magic('pinfo', 'Why')
X = 'iNeuron'

def func():

global X

X = 'NI'

func()

print(X)


# In[4]:


X = 'iNeuron'
def func():
    global X
    X = 'NI!'
    print(X)

func()
print(X)


# In[ ]:


get_ipython().set_next_input('5. What about this code—what’s the output, and why');get_ipython().run_line_magic('pinfo', 'why')


# In[ ]:


X = 'iNeuron'

def func():

X = 'NI'

def nested():

print(X)

nested()

func()

X


# In[5]:


X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
    
nested()
func()
X


# In[ ]:


get_ipython().set_next_input('6. How about this code: what is its output in Python 3, and explain');get_ipython().run_line_magic('pinfo', 'explain')
def func():

X = 'NI'

def nested():

nonlocal X

X = 'Spam'

nested()

print(X)

func()


# In[6]:


def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()


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




