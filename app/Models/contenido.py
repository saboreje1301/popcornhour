from flask_sqlalchemy import SQLAlchemy
from app.extensions import db


class Contenido(db.Model):
    __tablename__ = 'contenido'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    titulo_original = db.Column(db.String(255))
    titulo_espanol = db.Column(db.String(255))
    director = db.Column(db.String(255))
    genero = db.Column(db.String(50))
    anio = db.Column(db.Integer)
    duracion = db.Column(db.Integer)
    sinopsis = db.Column(db.Text)
    url = db.Column(db.Text)  
    
    def save_contenido(self):
        
        db.session.add(self)
        db.session.commit()

    def delete(self):
        
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        
        return f'<Contenido {self.titulo_espanol}>'

    def to_dict(self):
        
        return {
            'id': self.id,
            'tipo': self.tipo,
            'titulo_original': self.titulo_original,
            'titulo_espanol': self.titulo_espanol,
            'director': self.director,
            'genero': self.genero,
            'anio': self.anio,
            'duracion': self.duracion,
            'sinopsis': self.sinopsis,
            'url': self.url
        }
    
    def card(self):
        return {
            'url_image': self.url,
            'titulo_original': self.titulo_original,
            'titulo_espanol': self.titulo_espanol,
        }
        