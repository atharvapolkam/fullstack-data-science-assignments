#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Add the current date to the text file today.txt as a string.


# In[1]:


import datetime
from datetime import date
now = date.today()
cur_date = now.isoformat()
cur_date


# In[ ]:


with open('today.txt','w') as file:
    file.write(cur_date)


# In[ ]:


2. Read the text file today.txt into the string today_string


# In[ ]:


with open('today.txt','r') as file:
    today_string = file.read()
today_string


# In[ ]:


3. Parse the date from today_string.


# In[ ]:


from datetime import datetime
format = '%Y-%m-%d'
datetime.strptime(today_string,format)


# In[ ]:


4. List the files in your current directory


# In[ ]:


import os
for folders, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        print(file)


# In[ ]:


5. Create a list of all of the files in your parent directory (minimum five files should be available).


# In[ ]:


import os 
os.listdir()


# In[ ]:


6. Use multiprocessing to create three separate processes.
Make each one wait a random number of seconds between one and five, print the current time, and then exit.


# In[ ]:


import multiprocessing
import time 
import random
import datetime

def procOne():
    print(f'Proc_one_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_one_Endtime -> {datetime.datetime.now()}')
    
def procTwo():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')

def procThree():
    print(f'Proc_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Proc_two_Endtime -> {datetime.datetime.now()}')
    
if __name__ == "__main__":    
    p1 = multiprocessing.Process(target=procOne)
    p2 = multiprocessing.Process(target=procTwo)
    p3 = multiprocessing.Process(target=procThree)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


# In[ ]:


7. Create a date object of your day of birth.


# In[3]:


from datetime import datetime
my_dob = datetime.strptime('24/09/1998','%d/%m/%Y')
print(my_dob, type(my_dob))


# In[ ]:


get_ipython().set_next_input('8. What day of the week was your day of birth');get_ipython().run_line_magic('pinfo', 'birth')


# In[6]:


from datetime import datetime
my_dob = datetime(1998,9,24)
my_dob.strftime("%A")


# In[ ]:


get_ipython().set_next_input('9. When will you be (or when were you) 10,000 days old');get_ipython().run_line_magic('pinfo', 'old')


# In[ ]:


from datetime import datetime, timedelta
my_dob = datetime.strptime("12/01/1994",'%d/%m/%Y')
future_date = my_dob-timedelta(10000)
future_date


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





# In[ ]:




