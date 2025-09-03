import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wcc@2023")
    password = os.getenv("DATABASE_PASSWORD", "wcc@2023")
    encoded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"postgresql://postgres:{encoded_password}@127.0.0.1:5433/tarefas_3b")
    
    
    #SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SECRET_KEY@127.0.0.1:5433/tarefas_3b")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False