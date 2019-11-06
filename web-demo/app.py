from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, abort, flash
from flask_pymongo import PyMongo
from functools import wraps
from bson import ObjectId, json_util
import math
import json


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Hang-web'
app.config['MONGO_URI'] = 'mongodb+srv://nguyenthihang:<password>@cluster0-hwoih.gcp.mongodb.net/test'


mongo = PyMongo(app)


# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'username' in session:
#             return f(*args, **kwargs)
#         else:
#             next_url = request.url
#             login_url = '%s?next=%s' % (url_for('login'), next_url)
#             return redirect(login_url)
#     return wrap


# @app.route('/')
# def index():
#     slides = mongo.db.slide.find()
#     product_main = mongo.db.product.find()
#     news = mongo.db.news.find()
#     return render_template('index.html', slides = slides, product_main = product_main, news = news) 


# @app.route('/news')
# def news():
#     news = mongo.db.news.find()
#     return render_template('news.html', news = news) 

# @app.route('/addToCart/')
# def add_cart():

#     productId = request.args.get('productId')
#     product_cart = mongo.db.product.find_one({ '_id': ObjectId(productId)})
#     product_cart = json.loads(json_util.dumps(product_cart))
#     product_cart['qty'] = 1 
#     product_cart['total_price'] = int(product_cart['price'])



#     if 'cart' in session: 
#         cart_list = session['cart']
#         cart_list = json.loads(json_util.dumps(cart_list))
#         check = 0
#         for item in cart_list:
#             if item['_id']['$oid'] == productId:
#                 check = 1
#                 item['qty'] = item['qty'] + 1
#                 item['total_price'] = product_cart['total_price'] * item['qty']
#         if check == 0:
#             cart_list.append(product_cart)

#     else:
#         cart_list = []
#         cart_list.append(product_cart)

#     session['cart'] = cart_list

#     return redirect(url_for('cart'))


# @app.route('/cart')
# def cart():
#     if 'cart' not in session:
#         session['cart'] = [] 
        
#     cart = session['cart']
#     cart = json.loads(json_util.dumps(cart))

#     total = 0

#     price_item = []
    
#     for price in cart:
#         price_item.append(price['total_price'])

#     total = sum(price_item)

#     return render_template('cart.html', cart =  cart , total = total)

# @app.route('/remove-cart')
# def remove_cart():
#     session.pop('cart', None)
    
#     return redirect(url_for('cart'))

# @app.route('/checkout')
# @is_logged_in
# def checkout():
#     return  'checkout'


# @app.route('/admin/')
# @is_logged_in
# def admin():
#     return render_template('admin.html') 

# @app.route('/product-details/<string:id_product>' , methods=['GET'])
# def product_details(id_product):
#     detail_product = mongo.db.product.find_one({"_id": ObjectId(id_product)})
#     return render_template('product_details.html', detail_product = detail_product) 

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if 'username' not in session:
#         error = None
#         if request.method == 'POST':
#             user_login = mongo.db.admin.find_one({"username": request.form["username"], "password": request.form["password"] })
#             if user_login is None:
#                 error = "Khong dung mat khau hoac tai khoan"
#             else:
#                 session['username'] = request.form['username']
#                 return redirect(url_for('admin'))
                

#         return render_template('login.html', error=error)
    
#     else:
#         return "You logged in"



# @app.route('/logout')
# def logout():
# 	session.pop('username', None)
# 	return redirect('/')

@app.route('/index')
def index(): 
    hh = mongo.db.user.find({"admin": "admin"})
    for i in hh:
        print i
    return 'hghhg'
	

if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug=True)