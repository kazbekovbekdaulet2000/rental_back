import math
from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
from manager.models.clients.client import Client
from product.models.bag.bag import UserBag
from django.utils import timezone
from django.db.models.signals import post_save


class Order(AbstractModel):
    name = models.CharField(verbose_name=_('Имя заказчика'), max_length=255, null=False)
    phone = models.CharField(verbose_name=_("Телефон"), max_length=36, null=False)
    first_time_order = models.BooleanField(verbose_name=_("Заказ первый раз"), default=False)
    start_time = models.DateTimeField(verbose_name=_('Дата начала'))
    end_time = models.DateTimeField(verbose_name=_('Дата конца'))
    bag = models.ForeignKey(UserBag, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    approved = models.BooleanField(verbose_name=_("Принят"), default=False)
    address = models.CharField(verbose_name=_('Адрес доставки'), max_length=255, null=True)
    address_return = models.CharField(verbose_name=_('Адрес возврата'), max_length=255, null=True)
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.name}, {self.phone} ({self.created_at})"

    @property
    def total_time(self):
        return self.end_time - self.start_time

    @property
    def total_days(self):
        days = math.ceil(self.total_time.total_seconds() / (24 * 60 * 60))
        if (days == 0): 
            days = 1
        return days

    @property
    def total_price(self):
        return self.bag.total_price * self.total_days + self.bag.delivery_price + self.bag.delivery_back_price

    @property
    def services_price(self):
        return self.total_days * self.bag.services_price

    @property
    def products_price(self):
        return self.total_days * self.bag.products_price

    @property
    def telegram_message(self):
        def get_time(time):
            return timezone.localtime(time, timezone.get_fixed_timezone(360)).strftime(format_data)
        format_data = "%d.%m.%y / %H:%M"
        order = f"""<b>Заказ #{self.id}\n\n"""
        client = f"""Данные клиента:</b>\n\nИмя: <b>{self.name}</b>\n"""
        phone = f"""Номер телефона: <a href="tel:{self.phone}" className='phone'><b>{self.phone_prettify}</b></a>\n"""
        new_client = f"""Новый клиент: <b>{'да' if self.first_time_order else 'нет'}</b>\n"""
        delivery = f"""Доставка: <b>{'да' if self.bag.delivery else 'нет'}</b> <b>({str(self.bag.delivery_price + self.bag.delivery_back_price)+"KZT" if self.bag.delivery else ''})</b>\n"""
        address = f"""Адрес доставки: <b>{self.address}</b>\n""" if self.bag.delivery else ""
        address_return = f"""Адрес возврата: <b>{self.address_return}</b>\n""" if self.bag.delivery_back else ""
        start = f"""Начала аренды: <b>{get_time(self.start_time)}</b>\n"""
        end = f"""Конец аренды: <b>{get_time(self.end_time)}</b>\n\n"""
        return order + client + phone + new_client + delivery + address + address_return + start + end

    @property
    def phone_prettify(self):
        return self.phone.replace(" ", "").replace("(", "").replace(")", "")

    @property
    def telegram_message_footer(self):
        duriation = f"""\n\nСрок аренды: {self.total_days} суток\n"""
        sum = f"""<em>Сумма оплаты: {self.total_price}</em>"""
        return duriation + sum

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


def send_tg_message(sender, instance, created, **kwargs):
    pass


post_save.connect(send_tg_message, sender=Order)
