from django.db import models
from django.utils.translation import gettext_lazy as _


class InventoryTarifType(models.IntegerChoices):
    DEFAULT = 0, _("Обычная")
    SET = 1, _("В сете")


class ManagerOrderInventoryStatus(models.IntegerChoices):
    RESERVED = 0, _("Оборудование зарезервировано")
    INRENT = 1, _("Оборудование в аренде")
    ACCEPTED = 2, _("Оборудование принято")
    BROKEN = 3, _("Оборудование сломано")


class ManagerOrderType(models.IntegerChoices):
    RESERVED = 0, _("Зарезервировано")
    CANCELLED = 1, _("Отменен")
    INRENT = 2, _("В аренде")
    PARTIALLY_RETURNED = 3, _("Частично возвращен")
    RETURNED = 4, _("Возвращен")


class InventoryStatusType(models.IntegerChoices):
    FREE = 0, _("Свободно")
    RESERVED = 1, _("Зарезервировано")
    INREND = 2, _("В аренде")
    BROKEN = 3, _("Сломано")