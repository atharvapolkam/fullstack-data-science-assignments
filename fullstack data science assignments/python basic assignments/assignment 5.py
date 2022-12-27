#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')


# In[1]:


a={}


# In[2]:


type(a)


# In[ ]:


2. What is the value of a dictionary value with the key &#39;foo&#39; and the value 42?


# In[5]:


{'foo':42}


# In[6]:


value(a)


# In[ ]:


get_ipython().set_next_input('What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')

Most significant difference:
List - items in list are Ordered
Dictionary : iten in dictionary are unordered


# In[ ]:


What happens if you try to access spam['foo'] if spam is {'bar': 100}?


# In[7]:


spam={'bar' : 100}


# In[11]:


spam['bar']


# In[13]:


spam['foo']


# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
&#39;cat&#39; in spam.keys()?


# In[18]:


spam={'cat' : 100}
'cat' in spam
 


# In[20]:


'cat' in spam.keys()


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if &#39;color&#39; not in spam:
spam[&#39;color&#39;] = &#39;black&#39;


# In[26]:


spam={'cat':100}


# In[30]:


spam.setdefault('color','black')


# In[31]:


spam


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




