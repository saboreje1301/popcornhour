from flask import Blueprint, render_template, make_response, request, redirect, url_for, session
from flask_restful import Resource, Api
from flask import jsonify
from .Models.usuarios import User
from .methods import *
from .extensions import db
from .Models.contenido import Contenido
import random

app = Blueprint('main', __name__)
api = Api(app)


@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/moderador')
def moderador():
    return render_template('moderador.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


class Home(Resource):
    def get(self):
        cards = Contenido.query.all()
        random_cards = random.sample(cards, min(len(cards), 10))
        cards_data = [card.card() for card in cards]  # Convertir las instancias a diccionarios
        html_content = render_template('index.html', cards=cards_data, random_cards=random_cards)   
        return make_response(html_content)        
    
class Search(Resource):
    def get(self):
        query = request.args.get('query', '')  # Obtener el valor del input de búsqueda
        if query:
            results = Contenido.query.filter(
                Contenido.titulo_espanol.ilike(f'%{query}%') |
                Contenido.titulo_original.ilike(f'%{query}%')
            ).all()
            if results:
                html_busqueda = render_template('search.html', results=results, query=query)
            else:
                html_busqueda = render_template('search.html', query=query, no_results=True)
            return make_response(html_busqueda, 200)
        return make_response(render_template('search.html'))

    

class Login(Resource):
    def get(self):
        # Renderiza la plantilla y crea una respuesta HTML
        html_content = render_template('login.html')
        return make_response(html_content)
        
    def post(self):
        data = request.form
        email = data.get('email')
        password = data.get('password')

        respuesta, status = inicio_sesion(email, password)

        if status == 200:
            session['logged_in'] = True  # Establecer la variable logged_in en la sesión
            cards = Contenido.query.all()
            cards_data = [card.card() for card in cards]  # Convertir las instancias a diccionarios
            # Renderiza la plantilla y crea una respuesta HTML con los datos de las tarjetas
            html_content = render_template('index.html', cards=cards_data, logged_in=True)
            return make_response(html_content)
        else:
            return respuesta, status
                
class RegisterUser(Resource):

    def get(self):
        # Renderiza la plantilla y crea una respuesta HTML
        html_content = render_template('register.html')
        return make_response(html_content)

    def post(self):
        data = request.json  # Cambiado a request.json para recibir JSON
        username = data.get('username')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Validar que todos los campos estén presentes
        if not username or not name or not email or not password:
            return jsonify({'success': False, 'message': 'Please fill in all fields'})

        # Verificar si el usuario ya existe
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'User already exists'})

        # Crear un nuevo usuario
        new_user = User(username=username, name=name, email=email)
        new_user.set_password(password)  # Asumiendo que tienes un método para establecer la contraseña

        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'success': True, 'message': 'User registered successfully'})    

class Moderador(Resource):
    def get(self):
        html_content = render_template('moderador.html')
        return make_response(html_content)

    def post(self):
        try:
            tipo = request.form.get('tipo')
            titulo_original = request.form.get('titulo_original')
            titulo_espanol = request.form.get('titulo_espanol')
            director = request.form.get('director')
            genero = request.form.get('genero')
            anio = request.form.get('anio')
            duracion = request.form.get('duracion')
            sinopsis = request.form.get('sinopsis')
            url = request.form.get('url')

            campos = {
                "tipo": tipo,
                "titulo_original": titulo_original,
                "titulo_espanol": titulo_espanol,
                "director": director,
                "genero": genero,
                "anio": anio,
                "duracion": duracion,
                "sinopsis": sinopsis,
                "url": url
            }

            # Validación de datos
            campos_vacios = [campo for campo, valor in campos.items() if not valor]
            if campos_vacios:
                return {"error": f"Los siguientes campos son obligatorios: {', '.join(campos_vacios)}"}, 400

            respuesta, status = register_contenido(
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
            
            html_content = render_template('moderador.html', respuesta=respuesta)
            return make_response(html_content, status)

        except Exception as e:
            html_content = render_template('moderador.html', error=str(e))
            return make_response(html_content, 500)
        

class Contenido_site(Resource):
    def get(self, id):
        try:
            card = Contenido.query.get(id)
            if card is None:
                raise Exception("Card not found")

            card_content = {
                'id': card.id,
                'tipo': card.tipo,
                'titulo_original': card.titulo_original,
                'titulo_espanol': card.titulo_espanol,
                'director': card.director,
                'genero': card.genero,
                'anio': card.anio,
                'duracion': card.duracion,
                'sinopsis': card.sinopsis,
                'urlimage': card.urlimage
            }
            html_content = render_template('content.html', card_content=card_content)
            return make_response(html_content, 200)
        except Exception as e:
            html_content = render_template('moderador.html', error=str(e))
            return make_response(html_content, 500)


class APIRoutes:
    def init_routes(self, api):
        api.add_resource(Home, '/')
        api.add_resource(Login, '/login')
        api.add_resource(RegisterUser, '/register')
        api.add_resource(Moderador, '/moderador')
        api.add_resource(Contenido_site, '/content/<int:id>')
        api.add_resource(Search, '/search')

