from flask import Blueprint, flash, render_template, request, session, abort, redirect, url_for
import requests
from flask_pymongo import PyMongo
import os
from app import app
from bson import ObjectId, json_util
import math
import json

app.config['MONGO_DBNAME'] = 'Hang-web'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Hang-web'

mongo = PyMongo(app)

main_page = Blueprint('main_pages', __name__, url_prefix='/')

@main_page.route("/")
def index():
    admin_acc = {"username" : "admin", "password": "admin"}
    check = mongo.db.admin.find_one(admin_acc)
    if check == None:
        create_acc = mongo.db.admin.insert(admin_acc)

    slides = mongo.db.slide.find()

    product_main = mongo.db.product.find()
    news = mongo.db.news.find()
    return render_template('pages/index.html' , slides = slides, product_main = product_main, news = news)

@app.route('/addToCart/')
def add_cart():
    productId = request.args.get('productId')
    product_cart = mongo.db.product.find_one({ '_id': ObjectId(productId)})
    product_cart = json.loads(json_util.dumps(product_cart))
    product_cart['qty'] = 1 
    product_cart['total_price'] = int(product_cart['price'])



    if 'cart' in session: 
        cart_list = session['cart']
        cart_list = json.loads(json_util.dumps(cart_list))
        check = 0
        for item in cart_list:
            if item['_id']['$oid'] == productId:
                check = 1
                item['qty'] = item['qty'] + 1
                item['total_price'] = product_cart['total_price'] * item['qty']
        if check == 0:
            cart_list.append(product_cart)

    else:
        cart_list = []
        cart_list.append(product_cart)

    session['cart'] = cart_list

    return redirect(url_for('cart'))

@app.route('/product-details/<string:id_product>' , methods=['GET'])
def product_details(id_product):
    detail_product = mongo.db.product.find_one({"_id": ObjectId(id_product)})
    return render_template('product_details.html', detail_product = detail_product) 


@app.route('/cart')
def cart():
    if 'cart' not in session:
        session['cart'] = [] 
        
    cart = session['cart']
    cart = json.loads(json_util.dumps(cart))

    total = 0

    price_item = []
    
    for price in cart:
        price_item.append(price['total_price'])

    total = sum(price_item)

    return render_template('cart.html', cart =  cart , total = total)

@app.route('/remove-cart')
def remove_cart():
    session.pop('cart', None)
    
    return redirect(url_for('cart'))



@app.route('/checkout')
def checkout():
    return  'checkout'

@app.route('/category')
def category():
    product_main = mongo.db.product.find()

    product_category = mongo.db.category_product.find()


    return render_template('category.html', product_main = product_main, product_category = product_category )
