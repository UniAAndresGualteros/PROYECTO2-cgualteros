from flask import render_template, make_response
from flask_restful import Resource # type: ignore
from models.ingredientes import Ingredientes
from models.sabores import Sabores



class IngredientesController(Resource):
    
    def get(self):
        ingredientes = Ingredientes.query.join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).all()
        return make_response(render_template("ingredientes.html",ingredientes=ingredientes))
    
    """
    .join(TipoIngrediente, Ingredientes.tipoingrediente==TipoIngrediente.idTipo)
    .join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).
    """