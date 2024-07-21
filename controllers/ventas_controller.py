from flask import render_template, make_response
from flask_restful import Resource # type: ignore
from models.ventas import Ventas


class VentasController(Resource):
    
    def get(self):
        ventas = Ventas.query.all()
        return make_response(render_template("ventas.html",ventas=ventas))
    