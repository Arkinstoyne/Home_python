1. Модель
python
Копировать
Редактировать
# models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
2. Сид (создание заказов)
python
Копировать
Редактировать
# in shell or script
from django.contrib.auth.models import User
from app.models import Order

u = User.objects.first()
Order.objects.create(user=u, product="Ноутбук", quantity=1, price=150000)
Order.objects.create(user=u, product="Мышь", quantity=2, price=1500)
3. Представление
python
Копировать
Редактировать
# views.py
from django.shortcuts import render
from django.contrib.auth.models import User

def user_orders(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_orders.html', {'user': user})
4. Шаблон
html
Копировать
Редактировать
<!-- user_orders.html -->
<h2>Заказы {{ user.username }}</h2>
<ul>
  {% for order in user.orders.all %}
    <li>{{ order.product }} — {{ order.quantity }} шт. — {{ order.price }} ₽</li>
  {% endfor %}
</ul>