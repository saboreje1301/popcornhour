from config import db
from flask_restful import Resource, render_template
from methods import register_contenido


class Moderador(Resource):
    def get(self):
        return render_template('moderador.html')

    def post(self):
        tipo = db.Column(db.String(10), nullable=False)
        titulo_original = db.Column(db.String(255), nullable=False)
        titulo_espanol = db.Column(db.String(255), nullable=False)
        director = db.Column(db.String(255))
        genero = db.Column(db.String(255))
        anio = db.Column(db.Integer)
        duracion = db.Column(db.Integer)
        sinopsis = db.Column(db.Text)    

        respuesta, status = register_contenido(tipo=tipo, titulo_original=titulo_original, titulo_espanol=titulo_espanol, director=director, genero=genero, anio=anio, duracion=duracion, sinopsis=sinopsis)

        return respuesta, status