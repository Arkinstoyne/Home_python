from flask import Flask, request, render_template
from models import Product  # твоя модель
from app import app, db

@app.route('/products')
def products():
    # Получаем номер страницы из параметров запроса, по умолчанию 1
    page = request.args.get('page', 1, type=int)
    per_page = 10  # количество товаров на странице

    # Запрос с пагинацией
    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)

    products = pagination.items  # товары для текущей страницы

    return render_template('products.html', products=products, pagination=pagination)





