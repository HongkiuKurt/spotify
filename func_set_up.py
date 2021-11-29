#!/usr/bin/env python
# coding: utf-8

# In[1]:


import config
import pandas as pd
import numpy as np


# In[2]:


import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


# In[5]:


def set_up():
    a = input('Your database name.')
    song_database = pd.read_csv(a)
    return song_database
    


# In[ ]:


def scrap_song_by_artist(a):
    results = sp.search(q=a, limit=50,market="GB")
    for b in range(50):
        name = results["tracks"]["items"][b]['name']
        song = sp.search(q=name, limit=1,market="GB") 
        test = sp.audio_features(song["tracks"]["items"][0]["uri"])[0]
        test['artist'] = song["tracks"]["items"][0]['artists'][0]['name'].lower()
        test['song'] = song["tracks"]["items"][0]['name'].lower()
        song_database = song_database.append(test, ignore_index=True)
    return song_database


# In[ ]:


def get_playlist_tracks(username, playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id,market="GB")
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# In[ ]:


def get_artists_from_track(track):
    return [artist["name"] for artist in track["artists"]]


# In[ ]:


def get_artists_from_playlist(playlist_id):
    tracks_from_playlist = get_playlist_tracks("spotify", playlist_id)
    return list(set(artist for subset in [get_artists_from_track(track["track"]) for track in tracks_from_playlist] for artist in subset))


# In[1]:


def scrap_song_from_playlist():

    song_database = pd.read_csv('song_database.csv')
    name = input('input your playlist id.')
    get_playlist_tracks("spotify", name)

    new_artist_list = get_artists_from_playlist(name)
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
        
    song_database.drop_duplicates(subset=None, keep='first', inplace=True, ignore_index=False)
 


# In[ ]:




