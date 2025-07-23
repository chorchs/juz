from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Causa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_causa = db.Column(db.String(64), index=True, unique=True)
    tipo_causa = db.Column(db.String(64)) # Penal o No Penal
    fecha_inicio = db.Column(db.DateTime)
    victima_id = db.Column(db.Integer, db.ForeignKey('victima.id'))
    agresor_id = db.Column(db.Integer, db.ForeignKey('agresor.id'))

class Victima(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    apellido = db.Column(db.String(64))
    dni = db.Column(db.String(10), unique=True)
    fecha_nacimiento = db.Column(db.DateTime)
    domicilio = db.Column(db.String(128))
    telefono = db.Column(db.String(20))

class Agresor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    apellido = db.Column(db.String(64))
    dni = db.Column(db.String(10), unique=True)
    fecha_nacimiento = db.Column(db.DateTime)
    domicilio = db.Column(db.String(128))
    telefono = db.Column(db.String(20))
    reincidente = db.Column(db.Boolean, default=False)

class Pericia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    causa_id = db.Column(db.Integer, db.ForeignKey('causa.id'))
    tipo_pericia = db.Column(db.String(64))
    fecha_pericia = db.Column(db.DateTime)
    resultado = db.Column(db.Text)

class CamaraGesell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    causa_id = db.Column(db.Integer, db.ForeignKey('causa.id'))
    fecha_grabacion = db.Column(db.DateTime)
    psicologo = db.Column(db.String(128))
    transcripcion = db.Column(db.Text)
