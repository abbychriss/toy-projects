#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import plotly


# In[9]:


d = np.random.normal(loc = 20, scale = 0.125, size=10000000)


# In[10]:


plt.hist(d, bins=10000, color='#C39BD3')
plt.xlabel('Height (ft)')
plt.ylabel('Frequency')
plt.title('Height of Trees Histogram')
plt.show()


# In[ ]:


#My first histogram!


# In[ ]:




