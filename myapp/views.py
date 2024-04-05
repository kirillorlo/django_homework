import logging
from django.http import HttpResponse
from datetime import date, timedelta
from myapp.models import Order
from django.shortcuts import render, get_object_or_404

logger = logging.getLogger(__name__)


def home(request):
    html = """
    <h1>Добро пожаловать на сайт магазина "Рок-атрибутика"</h1>
    <p>Мы рады приветствовать вас!</p>
    <img src="https://cs10.pikabu.ru/post_img/2018/09/29/7/153821765616872994.jpg" alt="Рок-атрибутика">
    """
    logger.info('Посещение главной страницы магазина')

    return HttpResponse(html)


def about(request):
    html = """
    <h1>О нас</h1>
    <p>Магазин рок-атрибутики отличное место для всех рок-любителей, музыкантов и тех, кто любит особенный стиль. У нас вы найдете все необходимое, чтобы выразить свою страсть к рок-музыке и создать неповторимый образ. Посетите наш магазин и погрузитесь в мир рока уже сегодня!</p>
    """
    logger.info('Посещение страницы с описанием магазина')

    return HttpResponse(html)


def order_detail(request, client_id):
    order = get_object_or_404(Order, pk=client_id)
    return render(request, 'myapp/order_detail.html', {'order': order})

# def order_detail(request, client_id):
#     today = date.today()
#     last_week = today - timedelta(days=7)
#     last_month = today - timedelta(days=30)
#     last_year = today - timedelta(days=365)

#     orders_last_week = Order.objects.filter(client__id=client_id, order_date__range=[last_week, today]).distinct()
#     orders_last_month = Order.objects.filter(client__id=client_id, order_date__range=[last_month, today]).distinct()
#     orders_last_year = Order.objects.filter(client__id=client_id, order_date__range=[last_year, today]).distinct()

#     context = {
#         'orders_last_week': orders_last_week,
#         'orders_last_month': orders_last_month,
#         'orders_last_year': orders_last_year
#     }
#     return render(request, 'myapp/order_detail.html', context)
