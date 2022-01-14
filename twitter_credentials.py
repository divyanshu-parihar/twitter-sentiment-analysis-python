import os
# Importing environment Variables

from dotenv import load_dotenv

load_dotenv()
print(os.getenv('ACCES_TOKEN'))
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET') 