#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[11]:


import numpy as np
def p_class():
    y = np.array([[10,2,-1],[2,-5,-1],[-5,5,-1]])
    w = np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
    d = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
    c=1
    out=np.zeros((3,3))
    r=np.zeros((3,3))
    net=np.dot(y[0],np.transpose(w))
    print(net)
    out[0]=net
    out[0][out[0]>0]=1
    out[0][out[0]<=0]=-1
    r[0]=d[0]-out[0]
    del_w=0.5*np.dot(np.transpose(r),y)
    w=w+del_w
    print(w)
    return w
p_class()


# In[12]:


pip install numpy


# In[13]:


import numpy as np
def p_class():
    y = np.array([[10,2,-1],[2,-5,-1],[-5,5,-1]])
    w = np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
    d = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
    c=1
    out=np.zeros((3,3))
    r=np.zeros((3,3))
    net=np.dot(y[0],np.transpose(w))
    print(net)
    out[0]=net
    out[0][out[0]>0]=1
    out[0][out[0]<=0]=-1
    r[0]=d[0]-out[0]
    del_w=0.5*np.dot(np.transpose(r),y)
    w=w+del_w
    print(w)
    return w
p_class()


# In[ ]:




