#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
from sklearn import datasets # sklearn comes with some toy datasets to practise
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from matplotlib import pyplot
from sklearn.metrics import silhouette_score
import IPython


# In[2]:


song_database = pd.read_csv('song_database.csv')


# In[ ]:





# In[3]:


song_database.drop(columns = ['Unnamed: 0'], inplace = True)


# In[4]:


X = song_database._get_numeric_data()


# In[5]:


X = X[:500]


# In[6]:


X


# In[7]:


scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns = X.columns)
IPython.display(X.head())
print()
display(X_scaled_df.head())


# In[8]:


X_scaled_df.describe()


# In[ ]:


kmeans = KMeans(n_clusters=3, random_state=1234)
kmeans.fit(X_scaled_df)


# In[ ]:


kmeans.labels_


# In[ ]:


# assign a cluster to each example
labels = kmeans.predict(X_scaled_df)
# retrieve unique clusters
clusters = np.unique(labels)
# create scatter plot for samples from each cluster
for cluster in clusters:
    # get row indexes for samples with this cluster
    row_ix = np.where(labels == cluster)
    # create scatter of these samples
    pyplot.scatter(X.to_numpy()[row_ix, 0], X.to_numpy()[row_ix, 1])
    # show the plot
pyplot.show()


# In[ ]:


clusters = kmeans.predict(X_scaled_df)
#clusters
pd.Series(clusters).value_counts().sort_index()


# In[ ]:




