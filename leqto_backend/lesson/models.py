from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from user_leqto.models import User

# When model changed run "$> python3 manage.py makemigrations lesson"
# Then "$> python3 manage.py sqlmigrate lesson [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "lesson/migrations/0001_initial.py" where migration_number = 0001
# And finally run "$> python3 manage.py migrate"


class Country(models.Model):
    name = models.CharField(max_length=40)


class City(models.Model):

    name = models.CharField(max_length=40)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)


class Location(models.Model):

    longitude = models.FloatField()
    latitude = models.FloatField()

    street = models.CharField(max_length=256)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10, null=True, blank=True)


class School(models.Model):

    name = models.CharField(max_length=40)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)


class Room(models.Model):

    name = models.CharField(max_length=40)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True)


class PaymentType(ChoiceEnum):

    Cash = "Cash"
    Paypal = "Paypal"
    CreditCard = "CreditCard"
    ApplePay = "ApplePay"
    GooglePay = "GooglePay"


class Lesson(models.Model):

    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=256)
    description = models.CharField(max_length=64000)
    module = models.CharField(max_length=40)

    date_time = models.DateTimeField()

    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    room_id = models.ForeignKey(Room, blank=True, null=True, on_delete=models.DO_NOTHING)

    payment_type = EnumChoiceField(enum_class=PaymentType, default=PaymentType.Cash)

    tag = models.CharField(max_length=256, blank=True, null=True)


class Feedback(models.Model):

    rating = models.IntegerField()
    comment = models.CharField(max_length=2048, blank=True, null=True)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

