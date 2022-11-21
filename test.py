# pip3 install Mastodon.py
from mastodon import Mastodon


Mastodon.create_app(
     'SpaceNews',
     api_base_url = 'https://masto.ai',
     to_file = 'pytooter_clientcred.secret'
)
