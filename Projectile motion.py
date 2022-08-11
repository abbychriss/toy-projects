#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[1]:


import plotly
import matplotlib.pyplot as plt


# In[3]:


#Equations of motion:
#y = vt + .5a(t**2)
#x = vt
#y = x + 0.5a(x**2)/(v**2)


# In[6]:


#Let intial velocity v = 10 m/s, acceleration a = -9.8 m/s^2, and initial height h = 100 m


# In[11]:


def y(x, a, v, h):
    return x + (1/2)*a*(x**2)/(v**2) + h

xlist = np.linspace(0, 100, num = 1000, endpoint=True, retstep=False)
ylist = y(xlist, -9.8, 10, 100)
plt.figure(num=0, dpi=120)
plt.plot(xlist, ylist, color='pink')
plt.xlabel('Distance x (m)')
plt.ylabel('Height y (m)')
plt.title("Projectile Motion")


# In[ ]:





# In[ ]:




