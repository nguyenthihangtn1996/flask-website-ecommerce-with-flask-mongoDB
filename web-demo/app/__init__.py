from flask import Flask, render_template, url_for, redirect  
from flask_pymongo import PyMongo
import os

app = Flask(__name__)


app.config.from_object('config')

from app.admin_page.view import admin_page as admin_module
from app.main_page.view import main_page as page_module


app.register_blueprint(page_module)
app.register_blueprint(admin_module)

@app.errorhandler(404)
def not_found(error):  
    return render_template('404.html')