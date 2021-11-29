#!/usr/bin/env python
# coding: utf-8

# In[4]:


import config
import pandas as pd
import numpy as np
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
from matplotlib import pyplot
from IPython.display import IFrame


# In[12]:


##orginal song database.
def input_database():
    global song_database
    song_database = pd.read_csv('song_database.csv')
##Billboard top 100.
    global hot_list
    hot_list = pd.read_csv('top100_.csv')
##orginal song database with clusters.
    global database_cluster
    database_cluster = pd.read_csv('database_cluster.csv')
    return hot_list


# In[13]:


def wrong_search():
    database_cluster = pd.read_csv('database_cluster.csv')
    recommand_random = hot_list.sample()
    song_random = ''.join(recommand_random.song.values)
    artist_random = ''.join(recommand_random.artist.values)
    print('Your song can not be found in our database, let me recommand you a hit song', song_random.capitalize(), 'by', artist_random.capitalize())
    index_random = recommand_random.index
    track_id = song_database.loc[index_random, 'id'].values[0] 
    return track_id


# In[14]:


def hot_search():
    recommand_100 = hot_list.sample()
    song_100 = ''.join(recommand_100.song.values)
    artist_100 = ''.join(recommand_100.artist.values)
    print('Cool! Your song is in the top 100. Let me recommand another song from top 100. The song is', song_100.capitalize(), 'by', artist_100.capitalize())
    index_100 = recommand_100.index
    track_id = song_database.loc[index_100, 'id'].values[0]
    return track_id


# In[15]:


def cold_search():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id, client_secret= config.client_secret))
    selected_song = sp.search(q=song, limit=1,market="GB") 
    selected_song_feature = sp.audio_features(selected_song["tracks"]["items"][0]["uri"])[0]
    ##new_songlist = pd.read_csv('new_songlist.csv')
    model = load(filename = "Model/kmeans_7.pickle")
    scaler2 = load("Model/scaler.pickle")
    column_names = ['acousticness', 'danceability', 'duration_ms', 'energy',
       'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
       'speechiness', 'tempo', 'time_signature','valence']
    empty_database = pd.DataFrame(np.random.randint(0,1,size=(1, 13)), columns = column_names)
    for a in column_names:
        empty_database[a] = selected_song_feature[a]
    empty_database_scaled = scaler2.transform(empty_database)
    empty_database_scaled_df = pd.DataFrame(empty_database_scaled, columns = empty_database.columns)
    song_cluster = model.predict(empty_database_scaled_df)
    recommand_song = database_cluster[database_cluster['cluster'] == song_cluster[0]].sample()
    a = recommand_song.index
    track_id = song_database.loc[a, 'id'].values[0]
    return track_id


# In[16]:


def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as f: 
            return pickle.load(f) 
    except FileNotFoundError: 
        print("File not found!") 


# In[17]:


input_database()


# In[18]:


hot_list


# In[ ]:




