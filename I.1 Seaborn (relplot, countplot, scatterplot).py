#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import seaborn as sns


# In[4]:


data={'Name':['A','B','A','A','E'], 'Year':[2020,2012,2017,2019,2022], 'Total students':[8000,9000,10000,11000,12000],
      'type':['Rural','Urban','Rural','Urban','Rural']}


# In[5]:


import pandas as pd


# In[6]:


data_import=pd.DataFrame(data)


# In[7]:


data_import


# In[24]:


sns.scatterplot(x='Year',y='Total students',data=data_import, hue='type',hue_order=['Urban','Rural'])


# In[26]:


palette_colors={'Rural':'green','Urban':'blue'}


# In[31]:


sns.countplot(x='Name', data=data_import,hue='type',palette=palette_colors)


# In[33]:


#Visualizing 2 quantitative variables
#creating subplots with row and column
#(arranging in columns)
sns.relplot(x='Year',y='Total students', kind='scatter',col='type', data=data_import)


# In[35]:


#(arranging in rows)
sns.relplot(x='Year',y='Total students', kind='scatter',row='type', data=data_import, col_order=['Urban','Rural'])


# In[8]:


sns.relplot(x='Year',y='Total students', kind='scatter',row='type', data=data_import, col_order=['Urban','Rural'])


# In[12]:


#Make use of 'size' and 'hue' for easy visualization.
#hue and size take column name as input
#here name is categorical variable thats why different color of points, if 'Name' would have been quantitative variable then the color would have been same.
sns.relplot(x='Year',y='Total students',data=data_import, kind='scatter',size='Name',hue='Name')


# In[13]:


#'style' changes the representation of the points
sns.relplot(x='Year',y='Total students',data=data_import, kind='scatter',style='Name',hue='Name')


# In[15]:


#set alpha between 0 and 1
#0 being completely transparent and 1 being non transparent
sns.relplot(x='Year',y='Total students',data=data_import, kind='scatter',alpha=0.8,hue='Name')


# In[ ]:




