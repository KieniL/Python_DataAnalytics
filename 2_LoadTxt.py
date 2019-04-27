#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

#dtypes = {{'Sodium.mg.': int, 'Sugar.g.': int, 'Type': string}}
filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_1.txt"
data = pd.read_csv(filePath, sep = " ", header=0, decimal=",")
print(data.head())

data.dtypes


# In[19]:


filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_2.txt"
data = pd.read_csv(filePath, sep = " ", decimal=".")
print(data.head())

data.dtypes


# In[20]:


filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_3.csv"
data = pd.read_csv(filePath, sep = ",", decimal=".", header=0)
print(data.head())

data.dtypes


# In[21]:


filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_4.csv"
data = pd.read_csv(filePath, sep = ";", decimal=",", header=0)
print(data.head())

data.dtypes


# In[22]:


filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_5.dat"
data = pd.read_csv(filePath, sep = "-", decimal=".", header=0)
print(data.head())

data.dtypes


# In[23]:


filePath = "C:\\Users\\lkrei\\Desktop\\Python\\ExercisesDatenanalyse\\Datenanalyse\\Einheit 2\\cereal\\cereal_6.dat"
data = pd.read_csv(filePath, sep = ";", decimal=",")
print(data.head())

data.dtypes


# In[ ]:




