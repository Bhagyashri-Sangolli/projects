#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[8]:


data = pd.read_csv(r"C:\Users\Bhagyashri\Downloads\budget_23_24.csv", header = None)
column = ["Department /Ministry", "Fund allotted(in ₹crores)"]
data.columns = column


# In[9]:


data


# In[10]:


data.isnull().sum()


# In[11]:


# Assuming data is your DataFrame
data = data.iloc[[0, 8, 12, 15, 19, 24, 42, 43, 44], :]

# Adding a new row
new_row = pd.DataFrame({'Department /Ministry': ['OTHERS'], 'Fund allotted(in ₹crores)': [908439.39]})

# Concatenating the DataFrames
data = pd.concat([data, new_row], ignore_index=True)

# Displaying the updated DataFrame
print(data)


# In[12]:


data.isnull().sum()


# In[13]:


data.plot.bar(x = 'Department /Ministry', y = 'Fund allotted(in ₹crores)')


# In[14]:


df = data["Fund allotted(in ₹crores)"]
labels = data["Department /Ministry"]
plt.figure(figsize=(10,10))
plt.pie(df, labels=labels, autopct='%1.1f%%', startangle=80, pctdistance=0.9, shadow =False)
central_circle = plt.Circle((0, 0), 0.4, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=14)
plt.title("Distribution of The Budget", fontsize=20)
plt.show()


# In[ ]:




