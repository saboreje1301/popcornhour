import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:12345@172.18.112.1:5432/DBPopcornHour'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'b9a89ca1158c11cacb8339211eed0ba0'
    JWT_ALGORITIM = 'HS256'