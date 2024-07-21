from flask import render_template, make_response, request, redirect, url_for, flash
from flask_restful import Resource # type: ignore
from models.ingredientes import Ingredientes
from models.productos import Productos
from models.sabores import Sabores
from models.ventas import Ventas
from db import db


class HeladeriaController(Resource):
    
    def get(self):
        ingredientes = Ingredientes.query.join(Sabores, Ingredientes.sabor_base==Sabores.idSabor).all()
        productos = Productos.query.all()
        return make_response(render_template("index.html",ingredientes=ingredientes, productos=productos))
    
    
class SubmitSelection(Resource):
    def post(self):
        selected_ingredientes = request.form.getlist('ingredientes')
        selected_producto = request.form.get('producto')

        if not selected_producto or len(selected_ingredientes) > 3:
            flash("Error: Debe seleccionar un producto y hasta tres ingredientes.")
            return redirect(url_for('heladeriacontroller'))
        
        # Rellenar ingredientes con None si no se seleccionaron tres
        selected_ingredientes += [None] * (3 - len(selected_ingredientes))

        nueva_venta = Ventas(
            producto=selected_producto,
            ingrediente_1=selected_ingredientes[0],
            ingrediente_2=selected_ingredientes[1],
            ingrediente_3=selected_ingredientes[2],
            precio_base = 0,
            precio_plastico = 0,
            precio_total =0
        )

        try:
            db.session.add(nueva_venta)
            db.session.commit()
            flash("Venta registrada con éxito.")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al guardar la venta: {e}")

        return redirect(url_for('heladeriacontroller'))