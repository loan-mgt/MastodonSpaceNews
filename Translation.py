import requests 
from dotenv import load_dotenv
import os

load_dotenv()


auth_key =os.getenv('DEEP_KEY')

target_language = 'FR'


def traduction(text):

    
    result = requests.get( 
       "https://api-free.deepl.com/v2/translate", 
       params={ 
         "auth_key": auth_key, 
         "target_lang": target_language, 
         "text": text, 
       }, 
    ) 
    print("no traduction errror")
    return result.json()["translations"][0]["text"]


