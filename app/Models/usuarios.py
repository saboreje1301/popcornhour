from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db



class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Genera un hash de la contraseña y la guarda."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña proporcionada contra el hash almacenado."""
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email):
        """Obtiene un usuario por su correo electrónico."""
        return cls.query.filter_by(email=email).first()
    
    def save(self):
        """Guarda el usuario en la base de datos."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Elimina el usuario de la base de datos."""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Representación en cadena del objeto Usuario."""
        return f'<Name {self.name}>'

    def to_dict(self):
        """Convierte el objeto Usuario a un diccionario."""
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email
        }