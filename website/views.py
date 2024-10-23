from flask import Blueprint, render_template, request, redirect, url_for

#类似于创建一个controller
views = Blueprint('views', __name__)

# shopping cart
cart = []


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        cart.append(item)
    return redirect(url_for('views.view_cart'))


@views.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)


@views.route('/remove_item/<int:index>', methods=['POST'])
def remove_item(index):
    if 0 <= index < len(cart):
        cart.pop(index)
    return redirect(url_for('views.view_cart'))
