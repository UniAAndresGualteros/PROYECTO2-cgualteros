from flask import Flask, render_template
from dotenv import load_dotenv # type: ignore
from db import db
import os

from flask_restful import Api # type: ignore
from controllers.ingredientes_controller import IngredientesController
from controllers.productos_controller import ProductosController
from controllers.heladeria_controller import HeladeriaController
from controllers.heladeria_controller import SubmitSelection


load_dotenv()

secret_key = os.urandom(24)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)


api.add_resource(HeladeriaController, "/")
api.add_resource(SubmitSelection, '/submit_selection')
api.add_resource(IngredientesController, "/ingredientes")
api.add_resource(ProductosController, "/productos")
