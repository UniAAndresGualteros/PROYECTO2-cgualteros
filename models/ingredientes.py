from db import db

class Ingredientes(db.Model):
    idIngrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo_ingrediente = db.Column(db.String(15), nullable=False)
    sabor_base = db.Column(db.Integer, db.ForeignKey('sabores.idSabor'), nullable=False)
    
    sabores = db.relationship('Sabores', backref='ingredientes',lazy=True)
    
    
