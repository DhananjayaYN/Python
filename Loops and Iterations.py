for counter in [1,2,3,4,5]:
    print("This is a loop:counter=",counter)
    
total=0
for a in range(0,101,2):
    total=total+a
print('total=',total)

b=int(input("Enter number of times to repeat:"))
while(b!=0):
    print("Hello World!")
    b-=1
print("End")    

for x in range(0,4):
    for y in range(0,5):
        print('$', end='')
    print('')    
    
for i in range (-2,3):
   if i==0:
       continue
   print("5 Divided by",i,"is:",(5.0/i))
print("End")     
   
n=10
for i in range(0,n):
    print(i,"Hello")
    if(i==3):
        print("Count Aborted")
        break
    print(i,"Woerld!")
print("End of program")    

n=[2,4,5,10,13]
for i in n:
    print("Looking at:",i)
    if i==5:
        print("Found Number")
        break
else:
    print("Number not found")
print("End")

n=[1,4,8,16,17]
for i in n:
    print("Looking at:",i)
    if i==5:
        print("Found Number")
        break
else:
    print("Number not found")
print("End")

for fruit in fruits:
    # Not sure what to do!
print("Done")

for fruit in fruits:
    pass #Not sure what to do!
print("Done")