from bs4 import BeautifulSoup
import requests
import pandas as pd
import func_set_up
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import config
import numpy as np


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id, client_secret= config.client_secret))

func_set_up.scrap_song_from_playlist()
