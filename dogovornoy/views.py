from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


# №2 Шаблон главной страницы
def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'dogovornoy/index.html', context=context)


# Шаблон создание договоров
def create_dogovor(request):
    return render(request, 'dogovornoy/create_dogovor.html', {'menu': menu, 'title': 'Создание договора'})


# Добавление клиента договорной
def add_client(request):
    # добавление формы нового клиента c сохранением результата заполнения при неудаче
    if request.method == 'POST':
        form = AddKlientDogForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
                # kts.objects.create(**form.cleaned_data)
                form.save()
                return redirect('baza_dogovorov')
            # except:
            #     form.add_error(None, 'Ошибка добавления клиента')
    else:
        form = AddKlientDogForm()
    return render(request, 'dogovornoy/add_client.html', {'form': form, 'menu': menu, 'title': 'Новый клиент'})


# База клиентов договорного
def baza_dogovorov(request):
    klienty = kts.objects.all()
    context = {
        'klienty': klienty,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'dogovornoy/baza_dogovorov.html', context=context)


# 6 добавляем числовой индекс для разных компаний
def companies(request, comid):
    if (request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Компании</h1><p> {comid} </p>")


# 8 добавляем год в url
def archive(request, year):
    if int(year) > 2020:
        # 9 Вызов редиректа при условии
        return redirect('/', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# Страница 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сраница не найдена</h1>')


# Страница карточка клиента
def kartochka_klienta(request, klient_id):
    kartochka = get_object_or_404(kts, pk=klient_id)

    context = {
        'kartochka': kartochka,
        'menu': menu,
        'title': kartochka.dogovor_number,
    }

    return render(request, 'dogovornoy/kartochka_klienta.html', context=context)
