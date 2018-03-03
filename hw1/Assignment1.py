
# coding: utf-8

# In[8]:


import numpy as np
import math


# In[149]:


#non custom input
def observations():
    N = [10, 100, 1000]
    neat = np.random.normal(0, 1, (N[0], 1))        
    neat1 = np.random.normal(0,1,(N[1], 1))
    neat2 =np.random.normal(0,1,(N[2], 1))
    #mean for 10
    m1 = sum(neat) / 10
    v1 = neat.var()
    #mean for 100
    m2 = sum(neat1) / 100
    v2 = neat1.var()
    #mean for 1000
    m3 = sum(neat2) /1000
    v3 = neat2.var()
    print(m1)
    print(v1)
    print(m2)
    print(v2)
    print(m3)
    print(v3)
    


# In[150]:


observations()


# In[266]:


def observations2(mean, var, N):
    testboi = np.random.normal(mean, (var**.5), N)
    print(testboi.mean())
    print(testboi.var())
    return(testboi)
    


# In[276]:


print("TESTBOI2 = mean = 1, var = 4, N = 2000")
testboi2 = observations2(1,4,2000)
print("TESTBOI3 = mean =4, var = 9, N = 1000" )
testboi3 = observations2(4,9,1000)

x = newestArr = np.append(testboi2, testboi3)
print("X")
print(x.mean())
print(x.var())
    


# In[268]:


observations2(1,4,2000)

