#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
cric_data = np.loadtxt("cric.txt", skiprows = 1)
cric_data


# In[16]:


cric_data.shape


# In[22]:


s = cric_data[:,1]
d = cric_data[:,2]
I = cric_data[:,3
             ]
print(s)
print(d)
print(I)


# In[25]:


print(np.mean(s))
print(np.mean(d))
print(np.mean(I))


# In[27]:


print(np.median(s))
print(np.median(d))
print(np.median(I))


# In[30]:


print(np.average(s))
print(np.average(d))
print(np.average(I))


# In[ ]:




