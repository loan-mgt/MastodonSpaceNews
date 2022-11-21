# pip3 install Mastodon.py
# pip install python-dotenv
from mastodon import Mastodon
from dotenv import load_dotenv
import os

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