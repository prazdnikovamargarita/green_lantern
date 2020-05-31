from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required
from grocery_store.models import Good

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)

@main.route('/goods-page')
def goods_list():
    goods = Good.query.all()
    return render_template('goods.html', goods= goods)

@main.route('/orders')
@login_required
def orders():
    orders_list = []
    for order in current_user.orders:
        data = {
            "store": order.store.name,
            "date": order.created_time,
            "price": sum([good.good.price for good in order.order_lines]),
            "goods": {good.good.name: good.good.price for good in order.order_lines},
        }
        orders_list.append(data)
    totalsum = sum(order['price'] for order in orders_list)
    return render_template("orders.html", orders=orders_list, totalsum=totalsum)