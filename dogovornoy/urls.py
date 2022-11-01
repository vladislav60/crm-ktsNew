# №5 Создаём файл urls.py в приложении dogovornoy в него пишу

from django.urls import path, include, re_path
# Импорт всех пердставлений приложения
from .views import *


urlpatterns = [
    # Ссылка на главную страницу
    path('', index, name='home'),
    # Ссылка на страницу создание договора
    path('baza_dogovorov/', baza_dogovorov, name='baza_dogovorov'),
    # Ссылка на страницу Новый клиент
    path('add_client/', add_client, name='add_client'),
    # Ссылка на страницу Создать договор
    path('create_dogovor/', create_dogovor, name='create_dogovor'),
    # Ссылка на страницу Карточка клиента
    path('kartochka_klienta/<int:klient_id>/', kartochka_klienta, name='kartochka_klienta'),
    # Ссылка на договор Договор ОТС Квартира-дом физ.лицо
    # path('kv_ots_fiz/', kv_ots_fiz, name='kv_ots_fiz'),
]