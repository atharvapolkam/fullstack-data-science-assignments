#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to Add Two Matrices');get_ipython().run_line_magic('pinfo', 'Matrices')


# In[1]:



X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
    
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Multiply Two Matrices');get_ipython().run_line_magic('pinfo', 'Matrices')


# In[2]:



X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):
   
   for j in range(len(Y[0])):
      
       for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Transpose a Matrix');get_ipython().run_line_magic('pinfo', 'Matrix')


# In[3]:




X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]


for i in range(len(X)):

    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Sort Words in Alphabetic Order');get_ipython().run_line_magic('pinfo', 'Order')


# In[4]:


# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Remove Punctuation From a String');get_ipython().run_line_magic('pinfo', 'String')


# In[5]:


# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# In[ ]:





# In[ ]:





# In[ ]:




