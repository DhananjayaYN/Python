#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(choice) =="#":
     #program ends here
     print("Done. Terminating")
     sys.exit()
  else: 
     a=input("Enter first number: ")
     print(a)
     if (a)=="0$":
           continue
     b=input("Enter second number: ")
     print(b)
     if (b)=="0$":
           continue
     if (b)=="#":
           print("Done. Terminating")
           exit()
     
     if(choice) == '+':
           print(float(a),"+",float(b),"=",float(a)+float(b))
     if(choice)=="-":
           print(float(a),"-",float(b),"=",float(a)-float(b))
     if(choice)=="*":
           print(float(a),"*",float(b),"=",float(a)*float(b))
     if(choice)=="/":
           if(b)=="0":
               print("float division by zero")
               print(float(a),"/",float(b),"=","None")
           else:    
               print(float(a),"/",float(b),"=",float(a)/float(b)) 
     if(choice)=="^":
           print(float(a),"^",float(b),"=",float(a)^float(b))
     if(choice)=="%":
           print(float(a),"%",float(b),"=",float(a)%float(b)) 
     if(choice)=="$":
           print("Reset")
     


# In[ ]:




