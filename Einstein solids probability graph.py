#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import numpy as np
import matplotlib.pyplot as plt
import math
import gmpy2


# In[2]:


#Multiplicity of two Einstein solids in thermal contact
def multiplicity(n_a, n_b, q_a, q_tot):
    return ((gmpy2.factorial(q_a + n_a - 1))/((gmpy2.factorial(q_a))*(gmpy2.factorial(n_a - 1))))*(gmpy2.factorial(q_tot + n_b - q_a - 1))/((gmpy2.factorial(q_tot - q_a))*(gmpy2.factorial(n_b - 1)))


# In[8]:


#Function inputs number of oscillators on side A and B and the total number of energy quanta
#Outputs the probability distribution for the number of quanta on side A

def statmechgraph(n_a, n_b, q_tot):
    mults = []
    for i in range(0, q_tot):
        mults.append(int(multiplicity(n_a, n_b, i, q_tot)))

    probs = []
    for x in mults:
        a = (x / sum(mults))
        probs.append(a)
        
    max_prob = max(probs)
    max_quanta = probs.index(max_prob)
            
    print("Maximum probability is " + str(max(probs)) + " and max value for q_a is " + str(max_quanta)) 
    
    plt.plot(range(0,q_tot), probs, color = '#00CB1A')
    plt.xticks([max_quanta], ["max = "+str(max_quanta)])
    plt.xlabel('Energy quanta on side A')
    plt.ylabel('Probability')
    plt.title('Energy Distribution for two Einstein Solids in Thermal Contact')
    plt.show()


# In[9]:


statmechgraph(100, 200, 300)


# In[ ]:




