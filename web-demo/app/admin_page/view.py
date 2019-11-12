from flask import Blueprint, flash, render_template, request, session, abort, redirect, url_for, flash
from flask_pymongo import PyMongo
from functools import wraps
import requests
from bson import ObjectId, json_util
from werkzeug.utils import secure_filename

import os
from app import app

UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


admin_page = Blueprint('admin_pages', __name__, url_prefix='/admin')
app.config['MONGO_DBNAME'] = 'Hang-web'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Hang-web'

mongo = PyMongo(app)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('.login'))
    return wrap

    

@admin_page.route("/")
def admin_index():
    if 'username' in session:
        username = session['username']

        user_login = mongo.db.admin.find_one({"username": username})
    
    return render_template('admin/index.html', user_login = user_login )

@admin_page.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' not in session:
        error = ''
        if request.method == 'POST':
            user_login = mongo.db.admin.find_one({"username": request.form["username"], "password": request.form["password"] })
            if user_login is None:
                error = "Khong dung mat khau hoac tai khoan"
            else:
                session['username'] = request.form['username']
                return redirect(url_for('.admin_index'))
        return render_template('admin/login.html', error=error)
    
    else:
        flash('You logged in!')
        return redirect(url_for('.admin_index'))

@admin_page.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('.login'))



@admin_page.route("/product")
def admin_product():
    if 'username' in session:
        username = session['username']

        product_main = mongo.db.product.find()

        user_login = mongo.db.admin.find_one({"username": username})

    return render_template('admin/product.html', user_login = user_login, product_main = product_main )


@admin_page.route("/add-product")
def add_product():
    if 'username' in session:
        username = session['username']

        product_main = mongo.db.product.find()

        user_login = mongo.db.admin.find_one({"username": username})

    return render_template('admin/add_product.html', user_login = user_login)

@admin_page.route('/add', methods=['POST', 'GET'] )
def add():
    if request.method == 'POST':
        if 'upload_image' in request.files:
            file_image = request.files['upload_image']
            mongo.save_file(file_image.filename, file_image)
    
        
        add_item = mongo.db.product.insert_one({'name': request.form["name"], 'price': request.form["price"], 'category': 'quan' , 'sale_price' : request.form["sale_price"], 'image': file_image.filename, 'des': request.form["des"] })
        return redirect(url_for('.add_product'))

@admin_page.route('/update/<string:id_product>')
def update_page(id_product):
    detail_product = mongo.db.product.find_one({"_id": ObjectId(id_product)})
    # id_product = request.form['id_product']

    # update = mongo.db.product.update({"_id": ObjectId(id_product) },{"$set": {"name": "Quan", "price": 22 }})
    return render_template('admin/update.html', detail_product = detail_product)

@admin_page.route('/delete/' , methods=['POST'])
def delete():
    if 'username' in session:
        username = session['username']

        product_main = mongo.db.product.find()

        user_login = mongo.db.admin.find_one({"username": username})

    id_product = request.form['id_product']
    delete = mongo.db.product.delete_one({'_id': ObjectId(id_product)})

    return redirect(url_for('.admin_product'))