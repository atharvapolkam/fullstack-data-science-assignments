#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'.
Then, use the interactive interpreter to import the zoo module and call its hours() function.


# In[1]:


import zoo
zoo.hours()


# In[ ]:


2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.


# In[ ]:


import zoo as menagerie
menagerie.hours()


# In[ ]:


3. Using the interpreter, explicitly import and call the hours() function from zoo.


# In[ ]:


from zoo import hours
hours()


# In[ ]:


4. Import the hours() function as info and call it.


# In[ ]:


from zoo import hours as info
info()


# In[ ]:


5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.


# In[ ]:


plain = {'a': 1, 'b': 2, 'c': 3}
plain


# In[ ]:


get_ipython().set_next_input('6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain');get_ipython().run_line_magic('pinfo', 'plain')


# In[ ]:


#Yes
from collections import OrderedDict
fancy = OrderedDict(plain)
fancy


# In[ ]:


7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment.
Print dict_of_lists['a'].


# In[ ]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']


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




