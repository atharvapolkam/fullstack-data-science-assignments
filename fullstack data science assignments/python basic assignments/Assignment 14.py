#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What does RGBA stand for');get_ipython().run_line_magic('pinfo', 'for')
An RGBA value is a tuple of 4 integers, each ranging from 0 to 255.
The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.


# In[ ]:


get_ipython().set_next_input('2. From the Pillow module, how do you get the RGBA value of any images');get_ipython().run_line_magic('pinfo', 'images')
A function call to ImageColor.getcolor('CornflowerBlue', 'RGBA') will return (100, 149, 237, 255),
the RGBA value for that color.


# In[ ]:


get_ipython().set_next_input('3. What is a box tuple, and how does it work');get_ipython().run_line_magic('pinfo', 'work')
A box tuple is a tuple value of four integers: the left edge x-coordinate,
the top edge y-coordinate, the width, and the height, respectively.


# In[ ]:


get_ipython().set_next_input('4. Use your image and load in notebook then, How can you find out the width and height of an Image object');get_ipython().run_line_magic('pinfo', 'object')


# In[1]:


from PIL import Image
pic = Image.open('pic.png')
print(f'Width, Height -> {pic.size}') # Approach 1
print(f'Width, Height -> {pic.width},{pic.height}') # Approach 2
width,height = pic.size
print(f'Width, Height -> {width},{height}') # Approach 3


# In[ ]:


get_ipython().set_next_input('5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it');get_ipython().run_line_magic('pinfo', 'it')


# In[ ]:


from PIL import Image
img = Image.open('pic.png')
new_img = img.crop((0,50,50,50))


# In[ ]:


get_ipython().set_next_input('6. After making changes to an Image object, how could you save it as an image file');get_ipython().run_line_magic('pinfo', 'file')


# In[ ]:


from PIL import Image
pic = Image.open('pic.png')
pic.save('pic2.png')


# In[ ]:


get_ipython().set_next_input('7. What module contains Pillow’s shape-drawing code');get_ipython().run_line_magic('pinfo', 'code')
Pillows ImageDraw module contains Shape drawing methods.
The 'ImageDraw' module provides simple 2D graphics support for Image Object. 
Generally, we use this module to create new images, annotate or retouch existing
images and to generate graphics on the fly for web use.
The graphics commands support the drawing of shapes and annotation of text.


# In[ ]:


get_ipython().set_next_input('8. Image objects do not have drawing methods. What kind of object does');get_ipython().run_line_magic('pinfo', 'does')
get_ipython().set_next_input('How do you get this kind of object');get_ipython().run_line_magic('pinfo', 'object')
ImageDraw objects have shape-drawing methods such as
point(), line(), or rectangle().
They are returned by passing the Image object to the ImageDraw.Draw() function.

