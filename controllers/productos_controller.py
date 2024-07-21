from flask import render_template, make_response
from flask_restful import Resource # type: ignore
from models.productos import Productos


class ProductosController(Resource):
    
    def get(self):
        productos = Productos.query.all()
        return make_response(render_template("productos.html",productos=productos))
    