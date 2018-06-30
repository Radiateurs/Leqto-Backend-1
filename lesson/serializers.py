from rest_framework import serializers
from .models import Lesson, PaymentType
from enumchoicefield import EnumChoiceField


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id',
                  'title',
                  'sub_title',
                  'description',
                  'module',
                  'date_time',
                  'user_id',
                  'room_id',
                  'payment_type',
                  'tag']
        read_only_fields = ['user_id']

        payment_type = EnumChoiceField(enum_class=PaymentType)
