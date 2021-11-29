#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import config
import numpy as np


# In[8]:





# In[2]:


def scrap_from_playlist():
    list_id = input('Please input your playlist id.')
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id, client_secret= config.client_secret))
    song_database = pd.read_csv('song_database.csv')
    def get_playlist_tracks(username, playlist_id):
        results = sp.user_playlist_tracks(username,playlist_id,market="GB")
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    
    def get_artists_from_track(track):
        return [artist["name"] for artist in track["artists"]]
    
    def get_artists_from_playlist(playlist_id):
        tracks_from_playlist = get_playlist_tracks("spotify", playlist_id)
        return list(set(artist for subset in [get_artists_from_track(track["track"]) for track in tracks_from_playlist] for artist in subset))
    
    new_artist_list = get_artists_from_playlist(list_id)
    print(new_artist_list)
    
    for a in new_artist_list:
        results = sp.search(q=a, limit=50,market="GB")
    for b in range(50):
        try:
            name = results["tracks"]["items"][b]['name']
        except IndexError:
            pass
        except TypeError:
            pass
        song = sp.search(q=name, limit=1,market="GB") 
        try:
            test = sp.audio_features(song["tracks"]["items"][0]["uri"])[0]
        except IndexError:
            pass
        except TypeError:
            pass
        try:
            test['artist'] = song["tracks"]["items"][0]['artists'][0]['name'].lower()
        except TypeError:
            pass
        except IndexError:
            pass
        try:
            test['song'] = song["tracks"]["items"][0]['name'].lower()
        except TypeError:
            pass
        except IndexError:
            pass
        song_database = song_database.append(test, ignore_index=True)

    return song_database


# In[3]:





# In[3]:





# In[4]:





# In[ ]:




