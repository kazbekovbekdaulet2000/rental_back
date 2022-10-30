import math
from django.db import models
from common.custom_model import AbstractModel
from django.utils.translation import gettext_lazy as _
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
        return self.bag.total_price * self.total_days

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
        return f"""<b>Заказ #{self.id}\n\nДанные клиента:</b>\n\nИмя: <b>{self.name}</b>\nНомер телефона: <a href="tel:{self.phone}" className='phone'><b>{self.phone_prettify}</b></a>\nНовый клиент: <b>{'да' if self.first_time_order else 'нет'}</b>\nНачала аренды: <b>{get_time(self.start_time)}</b>\nКонец аренды: <b>{get_time(self.end_time)}</b>\n\n"""

    @property
    def phone_prettify(self):
        return self.phone.replace(" ", "").replace("(", "").replace(")", "")

    @property
    def telegram_message_footer(self):
        return f"""\n\nСрок аренды: {self.total_days} суток\n<em>Сумма оплаты: {self.total_price}</em>"""

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


def send_tg_message(sender, instance, created, **kwargs):
    pass


post_save.connect(send_tg_message, sender=Order)
