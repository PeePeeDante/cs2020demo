from flask import Flask;
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.salad
import codeitsuisse.routes.clean
import codeitsuisse.routes.inventory

