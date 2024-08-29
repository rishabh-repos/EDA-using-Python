#!/usr/bin/env python
# coding: utf-8

# # Zomato Dataset Exploratory Data Analysis

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


df = pd.read_csv('/Users/rishabhpandey/Downloads/Zomatodataset/zomato.csv', encoding = 'latin-1')


# In[18]:


df.head()
#calling a function that stores the data of first 5 rows of data set, its a method and has to be called with paranthesis


# In[17]:


df.columns
#it is an attribute or property of data thats why can be called without paranthesis


# In[19]:


df.info()
#objects basically means strings 


# In[21]:


df.describe()
#in this all the features that are taken into the consideration are integer or float, no catagorical or text feature are taken into considertion


# In[31]:


df.shape


# ## In Data Analysis what are things important 
# 1. Missing values
# 2. Explore about the numerical variable
# 3. Explore about the categorical Variable
# 4. Finding Relationship between Features

# In[22]:


df.isnull().sum()
#to determine the number of missing (or null) values in each column of a DataFrame.
#df.isnull() creates a DataFrame of True/False values indicating missing data.
#.sum() on this DataFrame counts True values (nulls) column-wise, giving the total number of missing values in each column.


# In[27]:


[features for features in df.columns if df[features].isnull().sum()>1]


# '''The list comprehension [features for features in df.columns if df[features].isnull().sum() > 1] is used to identify which columns in a pandas DataFrame (df) have more than one missing value (null or NaN). Let's break down each part of this expression:
# 
# Breaking Down the List Comprehension
# for features in df.columns:
# 
# This part of the list comprehension iterates over each column name (referred to as features) in the DataFrame df. df.columns returns an index object containing the column names of the DataFrame.
# 
# df[features]:
# For each iteration, df[features] accesses the column in the DataFrame corresponding to the current column name (features).
# 
# df[features].isnull():
# The .isnull() method is called on the column df[features] to create a boolean Series indicating where the missing values (nulls) are located. The result is True for missing values and False for non-missing values.
# 
# df[features].isnull().sum():
# 
# The .sum() method is called on the boolean Series returned by .isnull(). This converts True values to 1 and False values to 0, effectively counting the number of missing values in that column.
# 
# if df[features].isnull().sum() > 1:
# This condition checks whether the count of missing values in the column features is greater than 1. If this condition is true, the column name (features) will be included in the final list.'''

# In[74]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#there are 9 values in cuisines section which have null values , because the quantity is very small in comparision to total values , its not visible rn.


# In[35]:


df_country= pd.read_excel('/Users/rishabhpandey/Downloads/Zomatodataset/Country-Code.xlsx')


# In[36]:


df_country.head()


# In[38]:


df.columns
#country code is present in both file 
#we can combine both 


# In[41]:


final_df = pd.merge(df,df_country,on='Country Code',how='left')

#pd.merge(df, df_country, on='Country Code', how='left') performs a left join, 
#keeping all rows from df and adding matching rows from df_country based on the 'Country Code' column. 
#Rows in df without a match in df_country will have NaN in the resulting DataFrame for the columns from df_country.


# In[42]:


final_df.head()


# In[44]:


##to check  data type
final_df.dtypes


# In[45]:


final_df.columns


# In[49]:


final_df.Country.value_counts()
#this will find out how many diffrent countries are there and with respect to speific country, 
#how many records are there


# From this outcome we can deduce that zomato is mostly in india, followed by us

# In[52]:


country_names = final_df.Country.value_counts().index


# In[53]:


final_df.Country.value_counts().index


# In[54]:


final_df.Country.value_counts().values


# In[56]:


country_values = final_df.Country.value_counts().values


# In[57]:


## Pie chart
plt.pie(country_values,labels= country_names)


# In[59]:


## Pie chart - Top 3 countries that uses Zomato
plt.pie(country_values[:3],labels= country_names[:3])


# In[60]:


final_df.groupby(['Aggregate rating','Rating color','Rating text'])


# In[61]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size()


# In[64]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index()


# In[63]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[65]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# # observation
# 1. when the rating is between  4.5 to 4.9 -----> food is excelent
# 2. when the rating is between  4.0 to 4.4 -----> food is very good
# 3. when the rating is between  3.5 to 3.9 -----> food is good
# 4. when the rating is between  3.0 to 3.4 -----> food is average
# 5. when the rating is between  2.5 to 2.9 -----> food is below avergae
# 6. when the rating is between  2.0 to 2.4 -----> food is poor

# In[73]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x= "Aggregate rating", y= "Rating count", data=ratings)

#The x-axis shows different "Aggregate rating" categories.
#The y-axis shows the corresponding "Rating count" for each "Aggregate rating".
#The plot visually represents the relationship between aggregate ratings and their respective counts from the ratings DataFrame.


# In[76]:


#lets try to see the use of "hue"
sns.barplot(x= "Aggregate rating", y= "Rating count", data=ratings, hue = "Rating color")


# as we used hue , its not able to map the color or rating color to the color of bar plot 
# so we gonna use pallete for maping the colors
# 
# pallete is an attribute that is present in barplot where you can give your own color as it is required 

# In[81]:


sns.barplot(x= "Aggregate rating", y= "Rating count",hue = "Rating color",data=ratings, palette = ['white', 'red', 'orange', 'yellow', 'green', 'green'])


# # observations
# 1. not rated count is very high 
# 2. maximum number of ratings are between 2.5 to 3.4
# 

# In[ ]:





# # Count Plot

# In[85]:


sns.countplot(x='Rating color',data = ratings , palette =['white', 'red', 'orange', 'yellow', 'green', 'green'])
#y axis shows the frequency here


# In[84]:


ratings


# # find the countries name that has given 0 rating

#  to solve this we will use aggregate rating , aggregate rating of atleast one of the restaurant of the country 
#  must be zero

# In[88]:


final_df.columns


# In[93]:


final_df[final_df['Aggregate rating']=='0.0'].groupby('Country').size().reset_index()


# the code snippet final_df[final_df['Aggregate rating'] == '0'].groupby('Country').size().reset_index() is used to find the number of restaurants (or entries) in each country that have an aggregate rating of 0 
# 
# we dont want this

# In[96]:


final_df[final_df['Aggregate rating']=='0.0']


# In[98]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head()


# Observation
# 1. max 0 rating are from india

# # Find out which currencies is used in their respective country

# In[100]:


final_df.groupby(['Currency','Country']).size().reset_index()


# # Which country have online delivery

# In[104]:


final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts().reset_index()


# In[103]:


#another way of doing it 


# In[106]:


final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# # Observation
# 1. online deliveries are availbale in india and UAE

# # Create a Pie chart to find out cities destribution
# Top 5 only

# In[109]:


final_df.City.value_counts().index


# In[112]:


plt.pie(final_df.City.value_counts().values[:5],labels = final_df.City.value_counts().index[:5], autopct = '%1.2f%%')


# In[ ]:




