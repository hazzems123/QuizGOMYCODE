#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


url='https://drive.google.com/file/d/1YdbRKJZ0Kz742yDxIStLZIPIEUGlc1Cc/view'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]


# In[9]:


df = pd.read_csv(url2,sep=";")


# In[20]:


df.head()


# In[21]:


df.info(verbose=False)


# In[24]:


df.isnull().sum()


# In[25]:


df['Age'].fillna(df['Age'].mean(), inplace=True)


# In[26]:


print (df["Cabin"].value_counts())


# In[27]:


df["Cabin"].fillna('G6',inplace=True)


# In[29]:


print (df["Embarked"].value_counts())


# In[30]:


df["Embarked"].fillna('S',inplace=True)


# In[31]:


df.isnull().sum()


# In[32]:


import seaborn as sns
import matplotlib.pyplot as plt

grid = sns.FacetGrid(df, col = "Survived" ,row = "Sex" , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Age", bins = 20)


# In[34]:


grid = sns.FacetGrid(df, col = "Survived"  , row = "Embarked" ,size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[38]:



def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )


# In[39]:



plot_correlation_map(df)


# In[ ]:


#this graph simply means the correlation between each column against the other one , the values above zeros shows a positive correlation means when a value increase the other value increase as well, the values below zero means negative correlation , zero means no correlation between them.


# In[40]:


df.groupby(['Pclass', 'Survived']).mean()


# In[41]:


df.drop('Name',
  axis='columns', inplace=True)


# In[42]:


url='https://drive.google.com/file/d/1YdbRKJZ0Kz742yDxIStLZIPIEUGlc1Cc/view'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]


# In[43]:


df = pd.read_csv(url2,sep=";")


# In[47]:


title = [];
for i in df['Name'].str.split('.').str[0]:
    title.append(i)


# In[46]:


titles =[];
for i in title :
    titles.append(i.split(',', 1)[1])


# In[48]:


df.insert(1, "Title", titles, True)


# In[49]:


df.head()


# In[50]:


grid = sns.FacetGrid(df, col = "Title"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[51]:


Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer",

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty",

                  "the Countess": "Royalty",

                    "Dona":       "Royalty",

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs",

                    "Master" :    "Master"

                    }
    


# In[52]:


newTitles = []
for i in titles :
     i=i.lstrip()
     newTitles.append(Title_Dictionary[i])


# In[55]:


df.drop('Title',
  axis='columns', inplace=True)


# In[56]:


df.insert(1, "Title", newTitles, True)


# In[57]:


grid = sns.FacetGrid(df, col = "Title"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"Pclass", bins = 20)


# In[68]:


print (g)


# In[71]:





# In[76]:


Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer",

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty",

                  "the Countess": "Royalty",

                    "Dona":       "Royalty",

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs",

                    "Master" :    "Master"

                    }
    


# In[58]:


sum_column = df["Parch"] + df["SibSp"]
print (sum_column)


# In[59]:


df.insert(9, "FamilySize", sum_column, True)


# In[61]:


df.head()


# In[62]:


grid = sns.FacetGrid(df, col = "Survived"  , size = 2.2 , aspect = 1.6)
grid.map(plt.hist,"FamilySize", bins = 20)


# In[ ]:


#we found that most of the non survived are less than 1 they don't have families 


# In[ ]:





# In[ ]:





# In[ ]:




