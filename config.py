import os
class Config:
    SECRET_KEY = 'a72491'
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')