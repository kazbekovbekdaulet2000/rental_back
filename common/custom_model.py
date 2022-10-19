from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Создан'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Изменен'), auto_now=True)

    class Meta:
        abstract = True


class ContentTypeManager(models.Manager):
    def get_object_by_model(self, model: models.Model, id: int):
        return self.filter(
            content_type=ContentType.objects.get_for_model(model),
            object_id=id
        )

    def get_object_by_user(self, model: models.Model, id: int, user):
        return self.filter(
            content_type=ContentType.objects.get_for_model(model),
            object_id=id,
            owner=user
        )

    def get_user_objects(self, model: models.Model, user):
        return self.filter(
            content_type=ContentType.objects.get_for_model(model),
            owner=user
        )

    def exists(self, model: models.Model, user: User, object_id: int) -> bool:
        return self.filter(
            content_type=ContentType.objects.get_for_model(model),
            owner=user,
            object_id=object_id
        ).exists()


class ContentTypeModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = ContentTypeManager()

    class Meta:
        abstract = True


class ReactionsAbstract(models.Model):
    likes_count = models.PositiveIntegerField(
        verbose_name=_('Лайки'), default=0)
    comments_count = models.PositiveIntegerField(
        verbose_name=_('Комментарии'), default=0)
    reviews_count = models.PositiveIntegerField(
        verbose_name=_('Рейтинг'), default=0)
    bookmarks_count = models.PositiveIntegerField(
        verbose_name=_('Сохранения'), default=0)

    class Meta:
        abstract = True
