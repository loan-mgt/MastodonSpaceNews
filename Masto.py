# pip3 install Mastodon.py
# pip install python-dotenv
from mastodon import Mastodon
from dotenv import load_dotenv
import os
import requests

load_dotenv()

"""
Mastodon.create_app(
     'SpaceNews',
     api_base_url = 'https://masto.ai',
     to_file = 'pytooter_clientcred.secret'
)
"""



mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://masto.ai'
)
mastodon.log_in(
    'actunewspace@gmail.com',
    os.getenv('KEY'),
    to_file = 'pytooter_usercred.secret'
)


def tweet(img,msg):

    r = requests.get(img, allow_redirects=True)
    open('tmp.png', 'wb').write(r.content)
    
    m_id= mastodon.media_post("tmp.png")

    mastodon.status_post(msg,media_ids=[m_id])


if __name__=="__main__":
    url = "https://cdn.arstechnica.net/wp-content/uploads/2022/11/orion2.jpg"
    tweet(url,"#VTOL #SpaceX lancera Eutelsat-10B lors du dernier #VTOL du booster B1049.")