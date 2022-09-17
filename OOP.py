#!/usr/bin/env python
# coding: utf-8

# In[14]:


class fruit:
    number_of_items= None
    price_of_one_piece= None
    def __init__(self,x,y):
        self.number_of_items = x
        self.price_of_one_piece = y
       
    
class apple(fruit):
    def price(self):
       print("all apples price= Rs.",self.number_of_items*self.price_of_one_piece )
    
class banana(fruit):
    def price(self): 
        print("all banana price= Rs.",self.number_of_items*self.price_of_one_piece )
        
class orange(fruit):
    def price(self):
        print("all orange price= Rs.",self.number_of_items*self.price_of_one_piece)
        
myobject01= apple(10,20)
myobject02= banana(20,10)
myobject03= orange(5,45)

myobject01.price()
myobject02.price()
myobject03.price()


# In[ ]:




