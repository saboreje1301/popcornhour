import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.zmiigpbhudluulpmiioe:Rs82821301+@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'b9a89ca1158c11cacb8339211eed0ba0'
    JWT_ALGORITIM = 'HS256'