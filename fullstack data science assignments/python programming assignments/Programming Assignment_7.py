#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python Program to find sum of array');get_ipython().run_line_magic('pinfo', 'array')


# In[5]:


import array as arr
a = arr.array('i',[10, 21, 12, 13])
x=sum(a)
print(x)


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to find largest element in an array');get_ipython().run_line_magic('pinfo', 'array')


# In[ ]:


a = [10, 89, 9, 56, 4, 80, 8]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program for array rotation');get_ipython().run_line_magic('pinfo', 'rotation')


# In[6]:


def rotateArray(a,d):
    n=len(a)
    a[:]=a[d:n]+a[0:d]
    return a

arr = [1, 2, 3, 4, 5, 6]

print("Rotated list is")
print(rotateArray(arr,2)) 


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Split the array and add the first part to the end');get_ipython().run_line_magic('pinfo', 'end')


# In[8]:


def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to check if given array is Monotonic');get_ipython().run_line_magic('pinfo', 'Monotonic')


# In[9]:


def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False


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




