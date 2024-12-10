#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('../../Lenovo//datasets/Health_insurance.csv')


# In[4]:


df.head()


# In[5]:


df['sex']=df['sex'].apply(lambda x:1 if x=='female' else 0)
df['smoker']=df['smoker'].apply(lambda x:1 if x=='yes' else 0)


# In[6]:


df


# In[7]:


x = df[['age','bmi','children','sex','smoker']]
y = df['charges']


# In[14]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)


# In[11]:


test = {'age':[34,23,28],
        'bmi': [25.0,20,21],
        'children':[2,0,1], 
        'sex':['0','1','0'],
        'smoker':[0,0,1]}
test = pd.DataFrame(test)
test


# In[12]:


model.predict(test)



# In[13]:


q = [[34,25.0,2,0,0],[23,20.0,0,1,0],[28,21.0,1,0,1]]
model.predict(q)


# In[ ]:




