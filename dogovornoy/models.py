from django.db import models

# 9 Создание модели таблица договора
from django.urls import reverse


class kts(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Компания")
    dogovor_number = models.CharField(max_length=255, null=True, verbose_name="№ дог.")
    data_zakluchenia = models.CharField(max_length=255, null=True, verbose_name="Дата заключения")
    nalichiye_dogovora = models.CharField(max_length=100, blank=True, null=True, verbose_name="Наличие Договора")
    mat_otv = models.CharField(max_length=100, null=True, verbose_name="Мат.отв")
    act_ty = models.CharField(max_length=255, blank=True, null=True, verbose_name="Акты ТУ")
    time_reag = models.IntegerField(null=True, verbose_name="Время реагирования")
    yslovie_dogovora = models.CharField(max_length=255, blank=True, null=True, verbose_name="Условия договора")
    klient_name = models.TextField(null=True, verbose_name="Наименование Клиента")
    name_object = models.TextField(null=True, verbose_name="Наименование объекта")
    adres = models.TextField(null=True, verbose_name="Адрес объекта")
    iin_bin = models.CharField(max_length=255, null=True, verbose_name="ИИН/БИН")
    telephone = models.TextField(null=True, verbose_name="Телефон")
    vid_sign = models.CharField(max_length=255, null=True, verbose_name="Вид сигнализации")
    urik = models.BooleanField(default=False, null=True, verbose_name="ЮЛ")
    chasi_po_dog = models.IntegerField(null=True, verbose_name="Часы по договору")
    dop_uslugi = models.CharField(max_length=255, blank=True, null=True, verbose_name="Доп.услуги")
    abon_plata = models.IntegerField(null=True, verbose_name="Абон.плата")
    itog_oplata = models.IntegerField(blank=True, null=True, verbose_name="Итого")
    object_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="№ объекта")
    peredatchik_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="№ передатчика/GSM")
    stoimost_rpo = models.IntegerField(null=True, verbose_name="Стоимость РПО")
    date_podkluchenia = models.DateField(blank=True, null=True, verbose_name="Дата подключения")
    date_otklulchenia = models.DateField(blank=True, null=True, verbose_name="Дата отключения")
    gruppa_reagirovania = models.CharField(max_length=255, blank=True, null=True, verbose_name="Группа реагирования")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Электронный адрес")
    primechanie = models.TextField(blank=True, null=True, verbose_name="Примечание")
    agentskie = models.CharField(max_length=255, blank=True, null=True, verbose_name="Агентские")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото УДВ", blank=True, null=True)
    prochee = models.TextField(blank=True, null=True, verbose_name="Прочее")

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('kartochka_klienta', kwargs={'klient_id': self.pk})

    # Меняет название в админке
    class Meta:
        verbose_name = "База договоров"
        verbose_name_plural = "База договоров"
        ordering = ['-pk']
