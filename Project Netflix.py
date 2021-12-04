#!/usr/bin/env python
# coding: utf-8

# In[278]:


import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np


# In[143]:


#Quel est l'evolution de Netflix en terme de serie et de film depuis 2014 dans le monde ? 
 #Eliminer colonne -> show_id et description 


# In[144]:


data = pd.read_csv(r"C:\Users\kaurs\Documents\netflix_titles.csv")


# In[145]:


data.head(5)


# In[146]:


data.tail(5)


# In[147]:


#shape : number of rows and colums 
data.shape


# In[367]:


data.drop(columns=['show_id','description'])


# In[292]:


data.shape


# In[148]:


#Data type of each columns 
data.info()


# In[149]:


print("Is there any missing value?",data.isnull().values.any())


# In[150]:


data.isnull().sum().sum()


# In[151]:


data.isnull().sum()


# In[152]:


sns.heatmap(data.isnull(),cbar=False)
plt.title("Null values")
plt.show()


# In[153]:


per_missing=data.isnull().sum() * 100 / len(data)
per_missing


# In[154]:


data['director'].fillna('No director',inplace= True)
data['cast'].fillna('No cast',inplace= True)
data['country'].fillna('No country',inplace= True)
data.dropna(subset =['date_added','rating','duration'],inplace=True)


# In[155]:


data.isnull().any()


# In[156]:


data.shape


# In[157]:


dup_dat=data.duplicated().any()
print('Is there any duplicate value ?',dup_dat)


# In[158]:


data.describe()


# Analysis of Movies vs TV shows 

# In[159]:


plt.figure(figsize=(7,5))
sns.countplot(data.type,palette="pastel")
plt.xlabel('type (Movie or TV shows)')
plt.ylabel('Total count')
plt.title('Count of movies and TV shows')
plt.show()


# 2500 shows and 6000 movies . Movies are being the majority.

# Analysis of Movies vs TV shows in % 

# In[161]:


plt.figure(figsize=(10,7))
plt.pie(data.type.value_counts(),explode=(0.05,0.05),labels=data.type.value_counts().index,colors=['skyblue','#ffcc99'],autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('% of movies and TV shows')
plt.legend()
plt.show()


# In[162]:


#There are more movie titles with 69.7% than Tv shows titles with 30.3%


# In[163]:


#Is there more countains -13 in TV shows or Movies ? 


# Analysis Netflix movies and TV Shows ratings

# In[197]:


ratings_netflix=data.rating.value_counts()
ratings_netflix


# In[198]:


data['rating']=data['rating'].replace({'TV-MA':'+17','PG-13':'+13','TV-14':'+14','G':'Everyone','NC-17':'+17','R':'+17','TV-PG':'+17','TV-Y':'all age','TV-Y7':'+7','TV-Y7-FV':'Contains violence +7'})


# In[199]:


plt.figure(figsize=(17,10))
sns.countplot(data.rating,hue = data.type,palette="pastel")
plt.xlabel('Rating')
plt.ylabel('Total count')
plt.title('Rating of movies and TV shows')
plt.show()


# There is much more content for a mature audience for Movies. There is a slightly more TV shows for younger audience.

# Analysis countries with more content 

# In[200]:


data_per_country=data.country.str.strip().str.split(',',expand=True).stack()


# In[201]:


data_per_country=pd.Series(data_per_country.str.strip())


# In[202]:


data_per_country=data_per_country[data_per_country !='No country']
plt.figure(figsize=(8,8))
sns.countplot(y=data_per_country,order=data_per_country.value_counts().index[:10])
plt.xlabel('Titles')
plt.ylabel('Country')
plt.title('Top countries on Netflix')
plt.show()


# Films are produced in multiple contries as shown in the dataset. We separated all countries within a film before analysing the data.We removed the title with no countries. On the plot, we can see Top 10 countries which have the highest film and TV show production on Netflix. 
# The United States stands out on top because Netflix is an American company. India comes in second position followed by UK and Canada. 

# Analysis of pupular genres 

# In[204]:


data_per_theme=data.set_index('title').listed_in.str.strip().str.split(',',expand=True).stack().reset_index(level=1, drop=True)
data_per_theme=pd.Series(data_per_theme.str.strip())


# In[209]:


plt.figure(figsize=(8,8))
sns.countplot(y=data_per_theme,order=data_per_theme.value_counts().index[:10])
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.title('Top Genres on Netflix')
plt.show()


# In[296]:


category=data.listed_in.value_counts().head(15)
print(category)


# In[297]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
plt.title("Top movie categories")
sns.barplot(category,category.index)


# In terms of genres, International movies takes the first position followed by dramas and comedies. Even though the US has the most content on Nertflix, it looks like Netflix still like to put more International movies. 
# Maybe because Netflix most of the subscribers are not in US but they are interrnational subscribers.

# Sub data set of Movies 

# In[415]:


netflix_movies=data[data['type']=='Movie'].copy()
netflix_movies.head(5)


# Sub data set Tv shows

# In[175]:


netflix_shows=data[data['type']=='TV Show'].copy()
netflix_shows.head(5)


# In[217]:


year=data.date_added.value_counts().head(15)
year


# In[243]:


data['date_added'].value_counts().head(16).plot(kind='bar',color='red')
plt.xlabel('year')
plt.ylabel('Amount')


# In[266]:


netflix_shows['year_added'] =pd.DatetimeIndex(netflix_shows['date_added']).year


# In[267]:


netflix_shows_year = netflix_shows['year_added'].value_counts().to_frame().reset_index().rename(columns={'index':'year','year_added':'count'})
netflix_shows_year.sort_values(by=['year'], ascending=False)


# In[268]:


netflix_movies['year_added'] =pd.DatetimeIndex(netflix_movies['date_added']).year


# In[269]:


netflix_movies_year = netflix_movies['year_added'].value_counts().to_frame().reset_index().rename(columns={'index':'year','year_added':'count'})
netflix_movies_year.sort_values(by=['year'], ascending=False)


# In[270]:


data['year_added'] =pd.DatetimeIndex(data['date_added']).year


# In[283]:


netflix_year=data['year_added'].value_counts().to_frame().reset_index().rename(columns={'index':'year','year_added':'count'})
netflix_year=netflix_year[netflix_year.year!= 2008]
netflix_year.sort_values(by=['year'], ascending=False)


# In[284]:


netflix_year_type=data[['type','year_added']]
movie_per_year=netflix_year_type[netflix_year_type['type']=='Movie'].year_added.value_counts().to_frame().reset_index().rename(columns={'index':'year','year_added':'count'})
movie_per_year=movie_per_year[movie_per_year.year != 2008]
show_per_year=netflix_year_type[netflix_year_type['type']=='TV Show'].year_added.value_counts().to_frame().reset_index().rename(columns={'index':'year','year_added':'count'})
show_per_year=show_per_year[show_per_year.year != 2008]


# In[422]:


fig , ax= plt.subplots(figsize=(10,5))
sns.lineplot(data=netflix_year,x='year',y='count')
sns.lineplot(data=movie_per_year,x='year',y='count')
sns.lineplot(data=show_per_year,x='year',y='count')
ax.set_xticks(np.arange(2010,2020,1))
plt.title('Total content added each year')
plt.legend(['Total','Movie','Tv show'])
plt.ylabel('count')
plt.xlabel('year')
plt.show()


# As we can see on the plot, All contents have been tremendously added after 2014

# Maximum Content 

# In[416]:


netflix_movies['length']=netflix_movies['duration'].str.extract(r'(?P<length>\d+) min')


# In[417]:


netflix_movies['length']=netflix_movies['length'].astype(int)


# In[418]:


netflix_movies['length'].max()


# In[419]:


netflix_movies[netflix_movies['length']==netflix_movies['length'].max()]


# In[420]:


netflix_movies.duration.value_counts()


# More movies with 90 minutes 

# In[295]:


netflix_shows.duration.value_counts().head(20)


# In[381]:


data[data['duration'] == '11 Seasons']


# In[388]:


data[(data['duration'] == '1 Season') & (data['country']=='United States')].shape


# In[376]:


data_no_country=data[data['duration'].str.contains('Seasons')]


# In[389]:


data_no_country.shape


# In[421]:


data_no_country['duration'].value_counts().head(16).plot(kind='bar',color='red')
plt.xlabel('duration')
plt.ylabel('Amount')


# In[423]:


data_no_country=data[data['duration'].str.contains('1 Season')]
data_no_country=data_no_country[data_no_country.country !='No country']


# In[373]:


data_no_country.drop(columns =['show_id','description','cast','director','date_added'])


# In[344]:


data_per_countries=data[(data['duration'].str.contains('1 Season'))&(data['country'].str.contains('United States'))]


# In[345]:


data_per_countries


# In[353]:


netflix_shows.country.value_counts().drop('No country').head(5)


# In[351]:


netflix_movies.country.value_counts().drop('No country').head(5)

