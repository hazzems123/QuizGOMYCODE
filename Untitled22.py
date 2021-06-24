#!/usr/bin/env python
# coding: utf-8

# In[8]:


f=[]
for seq in range (2000,3200):
     if seq % 7 ==0 and seq % 5 != 0 :
        f.append(seq)
   


# In[9]:


print (f)


# In[10]:


n = 5

def fact (n) :
    if n ==1 :
        return n
    else:
        return n * fact (n-1)


# In[12]:


print (fact(n))


# In[ ]:


n = input ("please enter a value" )


# In[ ]:


dict = {}
def dictfunc (n) :
     if n ==1 :
        dict[n] = n
        return dict
     else :     
        x = n*n 
        dict[n]=x
       
        return dictfunc(n-1)
       
f =dictfunc(n)
print (f)


# In[ ]:




def missing_char(word,index) :
    
    x = list (word)
    x.pop(index)
    x= ''.join(x)
    print (x)
    return x
    


# In[ ]:


missing_char('kitten',1)


# In[ ]:



import numpy as np
arr = np.array([[0,1][2,3][4,5]])

print (arr)

arr= arr.tolist()

print (arr)


# In[ ]:


import numpy as np

x = np.array([[0, 1, 2], [2, 1, 0]])

print( np.cov(x))


# In[ ]:


import math
num = input()

numz = num.split(",")

print (numz)


c= 50
h = 30
outno = []
for i in numz :
    d = int(i)
    y= math.sqrt(2*c*d/h)
    y = round(y)
    outno.append(y)
    


# In[ ]:




