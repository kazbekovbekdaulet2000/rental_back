from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import date
from user.tasks import send_gmail
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'birth_date', 'description',
                  'country', 'city', 'user_type', 'password', 're_password', 'edu_place']
        extra_fields = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs['password']
        re_password = attrs['re_password']

        if password != re_password:
            raise serializers.ValidationError(
                {'password': 'Password must match'})
        min_date = date(1945, 1, 1)
        max_date = date(2017, 1, 1)
        if(attrs['birth_date'] < min_date or attrs['birth_date'] > max_date):
            raise serializers.ValidationError(
                {'birth_date': 'not match'})
        return attrs

    def save(self):
        del self.validated_data['re_password']
        account = User(
            **self.validated_data
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        send_gmail.delay(account.email)


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'image', 'name',
                  'surname', 'birth_date', 'city', 'description', 'verified', 'is_superuser']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'description',
                  'image', 'birth_date', 'city', 'user_type']
        read_only_fields = ['id', 'email']
