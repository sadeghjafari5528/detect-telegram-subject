import os

class Config(object):
    APP_ID = int(os.environ.get('APP_ID',1234567))
    API_HASH = os.environ.get('API_HASH',"3231uyc35find9ffe1yours12fe5q226")
    PORT= int(os.environ.get('PORT',5000))
    DATABASE_URL=os.environ.get('DATABASE_URL')