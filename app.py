from flask import Flask, render_template, request, flash, url_for, redirect
from sql_queries import ShopDB
from settings import*
app = Flask(__name__)
app.config['SECRET_KEY'] = 'nsgfnasgna'
db=ShopDB()

@app.route("/")
def index():
    categories=db.get_categories()
    items=db.get_all_items()
    print(items)
    return render_template("index.html",items=items)
@app.route("/item/<item_id>")
def item(item_id):
    item=db.get_item(item_id)
    return render_template("item.html",item=item)
@app.route("/category/<id>")
def category(id):
    items = db.get_all_items()
    return render_template("category.html", items=items)
@app.route("/order/<item_id>", methods=["GET","POST"])
def order(item_id):
    item=db.get_item(item_id)
    if request.method=="POST":
        try:
            db.add_order(item[0],request.form['name'],request.form['phone'],request.form['email'],item[5])
        except:
            flash("Помилка оформлення замовлення","alert-danger")
        flash("Додано замовлення","alert-light")
        return redirect(url_for('index'))
    
    return render_template("order.html",item=item)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
