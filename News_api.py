import requests 
import json


def get_news():
    result = requests.get( 
              "https://api.spaceflightnewsapi.net/v3/articles", 
             
    ) 
    rep  =result.text
    rep2 = json.loads(rep)
    return rep2