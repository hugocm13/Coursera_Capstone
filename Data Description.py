#!/usr/bin/env python
# coding: utf-8

# ## Data Description

# In[3]:


import pandas as pd
import numpy as np


# In[10]:


data = pd.read_csv(r'Downloads\Data-Collisions (1).csv', low_memory = False)


# In[13]:


data.dtypes


# I will be using data from car crashes in the USA that includes the collision type, along with other variables such as weather and time of day and speeding etc. This will enable me to build a predictive model for accident type. 
