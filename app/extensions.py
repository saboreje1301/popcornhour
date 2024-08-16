from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager # type: ignore

db = SQLAlchemy()

#Creamos una instancia de JWT extended
jwt = JWTManager()
