<<<<<<< HEAD
import os
=======
import os 
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    account_sid = 'AC905360593c371acea0ec4417770b3fd5'
    auth_token = 'd962e83a5a6c92b72a2530e705db61eb'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levi:eyeshadow@localhost/downtime'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://kiptim:jerotich@localhost/downtime'
    SECRET_KEY='DOWNTIME2018'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

config_options ={"production":ProdConfig,"default":DevConfig}
