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
    
    
    def es_sano(self) -> bool:
        if self.calorias < 100 or self.es_vegetariano:
            return True
        return False
        
    
    def abastecer(self):
        if self.tipo_ingrediente == 'Base':
            self.inventario += 5
        elif self.tipo_ingrediente == 'Complemento':
            self.inventario += 10
        else:
            raise ValueError("Tipo de ingrediente desconocido")

        db.session.commit()
        return f"Abastecimiento Completado"
    
    def renovar_inventario(self):
        if self.tipo_ingrediente =='Complemento':
            self.inventario = 0
            
        db.session.commit()
        return f"Inventario Renovado"