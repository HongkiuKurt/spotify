#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

## "https://www.billboard.com/charts/hot-100/"

def web_scraping():
    url = input('Please input url.')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    noother = soup.select("li > ul > li > h3")
    songname = []
    
    for a in range(len(noother)):
        b = noother[a].get_text().strip().lower()
        songname.append(b)
    
    artist = [elem.get_text() for elem in soup.find_all("span",{"class":"a-no-trucate"})]
    songer = []
    for a in artist:
        b = a.strip().lower()
        songer.append(b)
    
    top = pd.DataFrame(list(zip(songname, songer)),
               columns =['song', 'artist'])
    
    listen = input('What are you currently listening? ').lower()
    if listen in top.values:
        c = top.sample()
        print('Yes! Here is another hit song we recommand.' )
        print(''.join(c.song.values).capitalize(), 'by', ''.join(c.artist.values).capitalize())

    else:
        print('Your song is not hit, maybe another song?')
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




