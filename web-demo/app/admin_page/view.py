from flask import Blueprint, flash, render_template, request, session, abort, redirect, url_for
from flask_pymongo import PyMongo
from functools import wraps
import requests

import os
from app import app


admin_page = Blueprint('admin_pages', __name__, url_prefix='/admin')
app.config['MONGO_DBNAME'] = 'Hang-web'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Hang-web'

mongo = PyMongo(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('.login'))
    return wrap

@admin_page.route("/")
@is_logged_in
def admin_index():
    return render_template('admin/index.html')

@admin_page.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' not in session:
        error = None
        if request.method == 'POST':
            user_login = mongo.db.admin.find_one({"username": request.form["username"], "password": request.form["password"] })
            if user_login is None:
                error = "Khong dung mat khau hoac tai khoan"
            else:
                session['username'] = request.form['username']
                return redirect(url_for('hang'))
                

        return render_template('admin/login.html', error=error)
    
    else:
        return "You logged in"

@admin_page.route("/product")
def admin_product():
    return 'sdd'