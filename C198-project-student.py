#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : Ziyah ")
print("Will plot graphs to show which countries has the higher expenditure on health and higher life expectancy, Developed or Developing countries")


# # Task 1 - Show which countries has the higher expenditure on health, Developed or Developing countries

# In[2]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map.png') 
#predefine code end


# Developed Countries refers to the sovereign (independent) nation/state whose economy has highly progressed and possesses great technological infrastructure, as compared to other nations. The countries with low industrialization and low human development index are termed as developing countries.

# In[3]:


#import libraries and csv
import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv("Life_Expectancy_Data.csv")
df


# In[4]:


#Create a new dataframe only for country Australia which is a developed country
Australia_df = df.loc[df['Country']=='Australia']
Australia_df


# In[5]:


#Create a new dataframe only for country Italy which is a developed country
Italy_df=df.loc[df['Country']=='Italy']
Italy_df


# In[6]:


#Create a new dataframe only for country Brazil which is a developing country
Brazil_df=df.loc[df['Country']=='Brazil']
Brazil_df


# In[7]:


#Create a new dataframe only for country Colombia which is a developing country
Columbia_df=df.loc[df['Country']=='Colombia']
Columbia_df


# In[10]:


#Plot a line graph showing the Total expenditure on health of developed and developing countries
fig = plt.subplots(figsize=(12,8))
label = Australia_df['Year']
value = Australia_df['Total expenditure']
plt.plot(value,label,label="Australia",linewidth=3.0,color='purple')
label = Italy_df['Year']
value = Italy_df['Total expenditure']
plt.plot(value,label,label="Italy",linewidth=3.0,color='orange')
label = Brazil_df['Year']
value = Brazil_df['Total expenditure']
plt.plot(value,label,label="Brazil",linewidth=3.0,color='red')
label = Columbia_df['Year']
value = Columbia_df['Total expenditure']
plt.plot(value,label,label="Colombia",linewidth=3.0,color='yellow')
plt.xlabel('expenditure')
plt.ylabel('years')
plt.legend()
plt.show()


# Conclusion - The total expenditure of the developed countries are higher than those of developing countries

# # Task 2 Show which countries has the higher Life expectancy, Developed OR Developing countries

# In[11]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map2.png') 
#predefine code end


# The term “life expectancy” refers to the number of years a person can expect to live. By definition, life expectancy is based on an estimate of the average age that members of a particular population group will be when they die
# 

# In[12]:


fig = plt.subplots(figsize=(12,8))
label = Australia_df['Year']
value = Australia_df['Life expectancy']
plt.plot(value,label,label="Australia",linewidth=3.0,color='purple')
label = Italy_df['Year']
value = Italy_df['Life expectancy']
plt.plot(value,label,label="Italy",linewidth=3.0,color='orange')
label = Brazil_df['Year']
value = Brazil_df['Life expectancy']
plt.plot(value,label,label="Brazil",linewidth=3.0,color='red')
label = Columbia_df['Year']
value = Columbia_df['Life expectancy']
plt.plot(value,label,label="Colombia",linewidth=3.0,color='yellow')
plt.xlabel('Life expectancy')
plt.ylabel('years')
plt.legend()
plt.show()


# Conclusion - there is higher life expentancy in developed countries than in developing countries

# In[ ]:




