#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
x=turtle.Turtle()


# In[2]:


i=100


# In[3]:


for i in range(100,1,-5):
  x.pencolor('red')  
  x.circle(i)
  x.left(2)
  x.pencolor('blue')
  x.circle(i)
  x.left(2)
  x.pencolor('yellow')
  x.circle(i)
  x.left(10)
    


# In[4]:


x.pencolor('')
x.left(30)
x.forward(200)


# In[5]:


for i in range(100,1,-5):
  x.pencolor('red')  
  x.circle(i)
  x.right(2)
  x.pencolor('blue')
  x.circle(i)
  x.right(2)
  x.pencolor('yellow')
  x.circle(i)
  x.right(4)


# In[ ]:




