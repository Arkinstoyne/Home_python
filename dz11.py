from flask import Flask, request, jsonify

app = Flask(__name__)

# Простая имитация базы данных товаров
products = {
    1: {"name": "Товар 1", "quantity": 5},
    2: {"name": "Товар 2", "quantity": 20},
}


@app.route('/')
def home():
    return '''
        <h2>Каталог товаров</h2>
        <ul>
            <li>Товар 1 - <span id="qty-1">5</span> шт. <a href="#" onclick="updateQuantity(1, 10)">Добавить 10</a></li>
            <li>Товар 2 - <span id="qty-2">20</span> шт. <a href="#" onclick="updateQuantity(2, 10)">Добавить 10</a></li>
        </ul>
        <script>
            function updateQuantity(productId, quantity) {
                fetch('/update_quantity?id=' + productId + '&quantity=' + quantity)
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('qty-' + productId).innerText = data.new_quantity;
                    })
                    .catch(error => console.error('Ошибка:', error));
            }
        </script>
    '''


@app.route('/update_quantity', methods=['GET'])
def update_quantity():
    product_id = int(request.args.get('id'))
    quantity = int(request.args.get('quantity'))

    if product_id in products:
        products[product_id]['quantity'] += quantity
        return jsonify({"new_quantity": products[product_id]['quantity']})

    return jsonify({"error": "Товар не найден"}), 404


if __name__ == '__main__':
    app.run(debug=True)
