import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wcc@2023")
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:wcc@2023@127.0.0.1:5433/tarefas_3b")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 