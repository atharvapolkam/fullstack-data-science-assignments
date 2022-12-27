#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What advantages do Excel spreadsheets have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')
The Advantages of Excel over CSV are: 
    Excel (XLS and XLSX) file formats are better for storing and analysing complex data.
    An Excel not only stores data but can also do operations on the data using macros, formulas etc.
    CSV files are plain-text files, Does not contain formatting, formulas, macros, etc. It is also known as flat files.


# In[ ]:


get_ipython().set_next_input('2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')


# In[ ]:


import csv
with open('text.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# In[ ]:


import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


# In[ ]:


get_ipython().set_next_input('3. What modes do File objects for reader and writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')
For csv.reader(iterable_file_object), the file objects needed to be opened in read
mode mode='r' Whereas for csv.writer(iterable_file_object) the file objects needed
to be opened in write mode mode='w'.


# In[ ]:


get_ipython().set_next_input('4. What method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


import csv      
fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [ 
            ['Nitin', 'COE', '2', '9.0'], 
            ['kartik', 'COE', '2', '9.1'], 
            ['Ram', 'IT', '2', '9.3']
       ] 
with open("university_records.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)


# In[ ]:


get_ipython().set_next_input('5. What do the keyword arguments delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')
The delimiter argument changes the string used to separate cells in a row.
The lineterminator argument changes the string used to separate rows.


# In[ ]:


get_ipython().set_next_input('6. What function takes a string of JSON data and returns a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')
loads() method takes a string of JSON data and returns a Python data structure


# In[ ]:


get_ipython().set_next_input('7. What function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')
dumps() method takes a python data structure and returns a string of JSON data


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




