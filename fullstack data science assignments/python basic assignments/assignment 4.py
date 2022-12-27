#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?
empty list


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)


# In[3]:


spam = [2,4,6,8,10]


# In[4]:


spam[2] = 'hello'


# In[5]:


print(spam)


# In[ ]:


3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?


# In[6]:


spam[3] =d


# In[7]:


4. What is the value of spam[-1]?


# In[8]:


d


# In[9]:


5. What is the value of spam[:2]?
['a','b']


# In[10]:


bacon=[3.14,'cat','11','cat','True']


# In[11]:


print(bacon.index('cat'))


# In[16]:


bacon.append(99)


# In[17]:


bacon


# In[18]:


8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?


# In[19]:


bacon.remove('cat')


# In[20]:


bacon


# In[21]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')
+ and *


# In[22]:


10. What is difference between the list methods append() and insert()?


# In[23]:


While append() will add values only to the end of a list, insert() can add them anywhere in the list.


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:


The del statement and the remove() list method are two ways to remove values from a list.


# In[ ]:


12. Describe how list values and string values are identical.


# In[ ]:


Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, 
and be used with the in and not in operators.


# In[ ]:


13. What&#39;s the difference between tuples and lists?


# In[ ]:


Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists 
use the square brackets, [ and ]


# In[ ]:


How do you type a tuple value that only contains the integer 42?
(42)


# In[ ]:


15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?


# In[ ]:


The tuple() and list() functions, respectively


# In[ ]:




