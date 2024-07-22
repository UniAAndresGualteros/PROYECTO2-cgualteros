import unittest
from app import app, db
from models import Ingrediente

class IngredienteModelTestCase(unittest.TestCase):
    def setUp(self):
        """Configura el entorno para cada prueba."""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

        # Crear un ingrediente de prueba
        self.ingrediente = Ingrediente(nombre='Chocolate', precio=10.0, tipo_ingrediente='Base', inventario=0)
        db.session.add(self.ingrediente)
        db.session.commit()

    def tearDown(self):
        """Limpia el entorno después de cada prueba."""
        db.session.remove()
        db.drop_all()

    def test_abastecer_base(self):
        """Prueba el método abastecer para un ingrediente de tipo 'Base'."""
        ingrediente = Ingrediente.query.get(self.ingrediente.idIngrediente)
        ingrediente.abastecer()
        db.session.refresh(ingrediente)  # Actualiza la instancia desde la base de datos
        self.assertEqual(ingrediente.inventario, 5)

    def test_abastecer_complemento(self):
        """Prueba el método abastecer para un ingrediente de tipo 'Complemento'."""
        complemento = Ingrediente(nombre='Vainilla', precio=5.0, tipo_ingrediente='Complemento', inventario=0)
        db.session.add(complemento)
        db.session.commit()
        
        complemento.abastecer()
        db.session.refresh(complemento)  # Actualiza la instancia desde la base de datos
        self.assertEqual(complemento.inventario, 10)

    def test_abastecer_invalid_type(self):
        """Prueba el método abastecer para un tipo de ingrediente inválido."""
        ingrediente = Ingrediente(nombre='Fresa', precio=7.0, tipo_ingrediente='Unknown', inventario=0)
        db.session.add(ingrediente)
        db.session.commit()
        
        with self.assertRaises(ValueError):
            ingrediente.abastecer()

if __name__ == '__main__':
    unittest.main()