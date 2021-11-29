#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy 


# In[ ]:


#Quel est l'evolution de Netflix en terme de serie et de film depuis 2014 dans le monde ? 
 


# In[3]:


data = pd.read_csv(r"C:\Users\kaurs\Documents\netflix_titles.csv")


# In[5]:


data.head(5)


# In[6]:


data.tail(5)


# In[7]:


#shape : number of rows and colums 
data.shape


# In[8]:


#Data type of each columns 
data.info()


# In[9]:


print("Is there any missing value?",data.isnull().values.any())


# In[10]:


data.isnull().sum().sum()


# In[11]:


data.isnull().sum()


# In[12]:


sns.heatmap(data.isnull(),cbar=False)
plt.title("Null values")
plt.show()


# In[14]:


per_missing=data.isnull().sum() * 100 / len(data)
per_missing


# In[27]:


data['director'].fillna('No director',inplace= True)
data['cast'].fillna('No cast',inplace= True)
data['country'].fillna('No country',inplace= True)
data.dropna(subset =['date_added','rating','duration'],inplace=True)


# In[28]:


data.isnull().any()


# In[30]:


data.shape


# In[33]:


dup_dat=data.duplicated().any()
print('Is there any duplicate value ?',dup_dat)


# In[36]:


data.describe()


# In[45]:


plt.figure(figsize=(7,5))
sns.countplot(data.type,palette="pastel")
plt.xlabel('type (Movie or TV shows)')
plt.ylabel('Total count')
plt.title('Count of movies and TV shows')
plt.show()


# In[ ]:


# 2500 shows and 6000 movies . Movies are being the majority.


# In[69]:


plt.figure(figsize=(10,7))
plt.pie(data.type.value_counts(),explode=(0.05,0.05),labels=data.type.value_counts().index,colors=['skyblue','#ffcc99'],autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('% of movies and TV shows')
plt.legend()
plt.show()


# In[ ]:


#There are more movie titles with 69.7% than Tv shows titles with 30.3%


# In[ ]:


#Is there more countains -13 in TV shows or Movies ? 


# In[70]:


plt.figure(figsize=(17,10))
sns.countplot(data.rating,hue = data.type,palette="pastel")
plt.xlabel('Rating')
plt.ylabel('Total count')
plt.title('Rating of movies and TV shows')
plt.show()


# In[ ]:


#Comments on different subtitles 


# In[ ]:


#Data per countries 
#Erreur : des doublons -> Pays 


# In[28]:


data_per_country=data.country.str.strip().str.split(',',expand=True).stack()


# In[29]:


data_per_country=pd.Series(data_per_country.str.strip())


# In[34]:


data_per_country=data_per_country[data_per_country !='No country']
plt.figure(figsize=(8,8))
sns.countplot(y=data_per_country,order=data_per_country.value_counts().index[:10])
plt.xlabel('Titles')
plt.ylabel('Country')
plt.title('Top countries on Netflix')
plt.show()


# In[32]:


data_per_theme=data.set_index('title').listed_in.str.strip().str.split(',',expand=True).stack().reset_index(level=1, drop=True)
data_per_theme=pd.Series(data_per_theme.str.strip())


# In[35]:



plt.figure(figsize=(8,8))
sns.countplot(y=data_per_theme,order=data_per_theme.value_counts().index[:10])
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.title('Top Genres on Netflix')
plt.show()


# In[88]:


data.listed_in.unique()


# In[89]:


data.country.unique()

