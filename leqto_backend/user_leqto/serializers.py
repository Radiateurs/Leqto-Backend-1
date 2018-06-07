from rest_framework import serializers
from .models import UserLeqto


class UserLeqtoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLeqto
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'date_of_birth',
                  'facebook_link',
                  'google_link',
                  'phone_number',
                  'picture',
                  'payment_info']

    def create(self, validated_data):
        user = UserLeqto.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key is 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
