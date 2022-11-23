from django.shortcuts import get_object_or_404
from rest_framework import serializers
from product.models.bag.bag import UserBag
from product.models.bag.order import Order
from product.models.bot import BotUser
from product.tasks import send_telegram_message


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'first_time_order',
                  'start_time', 'end_time', 'comment', 'address', 'total_price', 'bag')
        read_only_fields = ('total_price', 'bag')

    def create(self, validated_data):
        validated_data['bag'] = get_object_or_404(
            UserBag, id=self.context['view'].kwargs['uuid'])
        res = super().create(validated_data)
        products = res.bag.products.all()
        services = res.bag.services
        txt = ""
        txt += res.telegram_message

        txt += """<b>Продукты:</b> \n"""

        for i in range(len(products)):
            txt += products[i].telegram_detail(i+1, res.total_days)

        txt += """<b>Сервисы:</b> \n"""
        for i in range(len(services)):
            txt += services[i].telegram_detail(i+1, res.total_days)

        if (res.comment):
            txt += f"""<b>Комментарии:</b> \n {res.comment} \n"""

        txt += (res.telegram_message_footer)

        for user in BotUser.objects.filter(approved=True):
            send_telegram_message.delay(user.user_id, txt)
        return res
