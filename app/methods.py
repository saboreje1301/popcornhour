from app.extensions import db
from .Models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import request, jsonify, render_template
from .Models.contenido import Contenido

# Configurar el logger


def inicio_sesion(email, password):
    user = User.get_user_by_email(email=email)
    caducidad = timedelta(minutes=60)

    if user and (user.check_password(password=password)):
        #Creamos token de acceso
        token_acceso = create_access_token(identity = user.username, expires_delta = caducidad)
        return {'Mensaje': 'Loggeado', 'Token': token_acceso}, 200
    return {'Error': 'Correo o contraseña no existen'}, 400

def user_register(username, name, email, password):
    try:
        if not username or not name or not email or not password:
            return {'Error': 'Todos los campos son requeridos'}, 400

        user = User.get_user_by_email(email=email)
        if user is not None:
            return {'Error': 'Este correo ya está registrado'}, 403

        nuevo_usuario = User(username=username, email=email, name=name)
        nuevo_usuario.set_password(password=password)
        nuevo_usuario.save()
        return {'message': 'Usuario registrado exitosamente'}, 200
    except Exception as e:
        return {'Error': f'Error del servidor: {str(e)}'}, 500
    

def register_contenido(tipo, titulo_original, titulo_espanol, director, genero, anio, duracion, sinopsis, url):
    try:
        nuevo_contenido = Contenido(
            tipo=tipo,
            titulo_original=titulo_original,
            titulo_espanol=titulo_espanol,
            director=director,
            genero=genero,
            anio=anio,
            duracion=duracion,
            sinopsis=sinopsis,
            url=url
    )
        nuevo_contenido.save_contenido()
        return {"message": "Contenido registrado exitosamente", "status": "success"}, 200
    except Exception as e:
        return {"error": str(e), "status": "error"}, 500
    

def fill_cards(titulo_original, titulo_espanol, url):
    try:
        card_main = Contenido(
            titulo_original=titulo_original,
            titulo_espanol=titulo_espanol,
            url=url,
            
        )
        db.session.add(card_main)  # Agregar la instancia a la sesión
        db.session.commit()  # Confirmar la transacción
        return {"message": "Tarjeta registrada exitosamente", "status": "success"}, 200
    except Exception as e:
        db.session.rollback()  # Revertir la transacción en caso de error
        return {"error": str(e), "status": "error"}, 500

