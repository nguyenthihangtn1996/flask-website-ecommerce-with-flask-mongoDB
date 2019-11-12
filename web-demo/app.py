
# @app.route('/news')
# def news():
#     news = mongo.db.news.find()
#     return render_template('news.html', news = news) 


from app import app

if __name__ == '__main__':
    app.run()