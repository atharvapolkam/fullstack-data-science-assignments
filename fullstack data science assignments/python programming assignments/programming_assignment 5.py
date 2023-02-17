#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Write a Python Program to Find LCM');get_ipython().run_line_magic('pinfo', 'LCM')


# In[7]:


a=int(input("enter first no:"))
b=int(input("enter second no:"))
maxNum=max(a,b)

while(True):
    if(maxNum%a==0 and maxNum%b==0):
        break
    maxNum=maxNum+1
print(f"lcm is {maxNum}")


# In[ ]:


get_ipython().set_next_input('Write a Python Program to Find HCF');get_ipython().run_line_magic('pinfo', 'HCF')


# In[10]:


a=int(input("enter first no:"))
b=int(input("enter second no:"))
mn=min(a,b)

for i in range(1,mn+1):
    if(a%i==0 and b%i==0):
        hcf=i
print(f"hcf/gcd is {hcf}")


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal');get_ipython().run_line_magic('pinfo', 'Hexadecimal')


# In[14]:


dec=int(input("enter a number which we want to convert:"))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program To Find ASCII value of a character');get_ipython().run_line_magic('pinfo', 'character')


# In[20]:


CHARACTER=input("enter a character:")
conversion=ord(CHARACTER)
print(conversion)


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations');get_ipython().run_line_magic('pinfo', 'operations')


# In[31]:


print("_____simple calculator_____")
a=float(input("enter first number: "))
b=float(input("enter second number: "))
print(" press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
choice=int(input("enter your choice from 1-4 :"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif(choice==3):
    print(a*b)
elif(choice==4):
    print(a/b)
else:
    print("invalid choice")


# In[ ]:




