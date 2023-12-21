#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/apoorvavinod46/The-Sparks-Foundation-Internship/blob/main/Task4_Exploratory_Data_Analysis_Terrorism.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# **THE SPARKS FOUNDATION**
# **#GRIPDECEMBER2023**

# **Author:Sed Ansar Ahmed Yaqoob, DATA SCIENCE & BUSINESS ANALTYTICS INTERN**

# **Task-4 Exploratory Data Analysis - ‘Terrorism’**

# Perform ‘Exploratory Data Analysis(Intermediate Level)’ on dataset ‘Terrorism’
# As a security/defense analyst,finding the hot zone of terrorism.

# Dataset: https://bit.ly/2TK5Xn5

# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# In[50]:


data = pd.read_csv("C:\\Users\\SYED ANSAR AHMED\\OneDrive\\Desktop\\globalterrorismdb_0718dist.csv",encoding='latin1')
data.head()


# In[14]:


data.columns.values


# In[16]:


data.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City','latitude':'latitude',
    'longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound'},inplace=True)


# In[17]:


data = data[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill',
               'Wound','target1','summary','Group','Targettype','Weapon','motive']]


# In[18]:


data.head()


# In[19]:


data.shape


# In[20]:


data.isnull().sum()


# In[21]:


data['Wound'] = data['Wound'].fillna(0)
data['kill'] = data['kill'].fillna(0)


# In[22]:


data.info()


# In[23]:


data.describe()


# In[24]:


year = data['Year'].unique()
years_count = data['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,
           y = years_count,
           palette = "tab10")
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year',fontsize=20)
plt.ylabel('Number of Attacks Each Year',fontsize=20)
plt.title('Attacks In Years',fontsize=30)
plt.show()


# In[25]:


pd.crosstab(data.Year, data.Region).plot(kind='area',stacked=False,figsize=(20,10))
plt.title('Terrorist Activities By Region In Each Year',fontsize=25)
plt.ylabel('Number of Attacks',fontsize=20)
plt.xlabel("Year",fontsize=20)
plt.show()


# In[26]:


attack = data.Country.value_counts()[:10]
attack


# In[27]:


data.Group.value_counts()[1:10]


# In[45]:


plt.subplots(figsize=(20, 10)
sns.barplot(x=data['Country'].value_counts()[:10].index, y=data['Country'].value_counts()[:10].values, palette='YlOrBr_r')
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=50)
plt.show()


# In[31]:


df = data[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4)
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# In[32]:


data['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(20,10),color='blue')
plt.xticks(rotation = 50)
plt.xlabel("City",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Top 10 most effected city",fontsize=20)
plt.show()


# In[33]:


data[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['darkslateblue'])
plt.xticks(rotation=50)
plt.title("Number of killed ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[34]:


data[['Attacktype','Wound']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['cyan'])
plt.xticks(rotation=50)
plt.title("Number of wounded  ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[48]:


plt.subplots(figsize=(20, 10))

sns.countplot(x=data["Targettype"], order=data['Targettype'].value_counts().index, palette="gist_heat", edgecolor=sns.color_palette("mako"))

plt.xticks(rotation=90)
plt.xlabel("Target Type", fontsize=15)
plt.ylabel("Count", fontsize=15)
plt.title("Distribution of Target Types", fontsize=20)
plt.show()


# In[36]:


data['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='green',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("Attack number",fontsize=15)
plt.show()


# In[37]:


data[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='yellow',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("No of killed people",fontsize=15)
plt.show()


# In[38]:


df=data[['Group','Country','kill']]
df=df.groupby(['Group','Country'],axis=0).sum().sort_values('kill',ascending=False).drop('Unknown').reset_index().head(10)
df


# In[39]:


kill = data.loc[:,'kill']
print('Number of people killed by terror attack:', int(sum(kill.dropna())))


# In[40]:


typeKill = data.pivot_table(columns='Attacktype', values='kill', aggfunc='sum')
typeKill


# In[41]:


countryKill = data.pivot_table(columns='Country', values='kill', aggfunc='sum')
countryKill


# **Conclusion and Results :**
# * Country with the most attacks: Iraq
# * City with the most attacks: Baghdad
# * Region with the most attacks: Middle East & North Africa
# * Year with the most attacks: 2014
# * Month with the most attacks: 5
# * Group with the most attacks: Taliban
# * Most Attack Types: Bombing/Explosion

# **Thank You!**

# In[ ]:





# In[ ]:




