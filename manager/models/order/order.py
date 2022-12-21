from django.db import models
from common.custom_model import AbstractModel
from manager.constants import ManagerOrderType
from manager.models.clients.client import Client
from product.models.bag.order import Order
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


class ManagerOrder(AbstractModel):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    status = models.PositiveIntegerField(
        default=ManagerOrderType.RESERVED,
        choices=ManagerOrderType.choices
    )

    total_price = models.PositiveIntegerField(null=False)
    products_price = models.PositiveIntegerField(null=False)
    services_price = models.PositiveIntegerField(null=False)

    rent_start = models.DateTimeField(null=True)
    rent_end = models.DateTimeField(null=True)


@shared_task(time_limit=600)
def metricst_update():
    logger.info('changed')


def on_order_change(sender, instance, created, **kwargs):
    metricst_update.delay()


post_save.connect(on_order_change, sender=ManagerOrder)
