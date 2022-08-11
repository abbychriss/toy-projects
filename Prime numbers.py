#!/usr/bin/env python
# coding: utf-8

# Inputs an integer and returns 'prime' or 'not prime'

# In[3]:


def primetest(n):
    for i in range(2, int(n/2)):
        if n%i == 0: return 'not prime'
        if n%i != 0: continue
        else: return 'prime'


# In[4]:


print(primetest(15))


# Inputs an integer and returns a list of the prime numbers less than that number

# In[7]:


def primeslessthan(n):
    primes = []
    for i in range(2,n):
        if primetest(i) == 'not prime': continue
        else: primes.append(i)
    return primes
    print(primes)


# In[8]:


primeslessthan(33)


# In[ ]:





# In[ ]:




