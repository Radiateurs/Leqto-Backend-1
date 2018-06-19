from django.db import models
from enum import Enum
from leqto_backend.user_leqto.models import User

# When model changed run "$> python3 manage.py makemigrations lesson"
# Then "$> python3 manage.py sqlmigrate lesson [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "lesson/migrations/0001_initial.py" where migration_number = 0001
# And finally run "$> python3 manager.py migrate"


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
    location_id = models.OneToOneField(Location, on_delete=models.CASCADE)
    school_id = models.OneToOneField(School, on_delete=models.CASCADE, null=True)


class PaymentType(Enum):

    Cash = 1
    Paypal = 2
    CreditCard = 3
    ApplePay = 4
    GooglePay = 5


class Lesson(models.Model):

    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=256)
    description = models.CharField(max_length=64000)
    module = models.CharField(max_length=40)

    date_time = models.DateTimeField()
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE)

    payment_type = models.IntegerField(choices=PaymentType, default=PaymentType.Cash)
    tag = models.CharField(max_length=256, blank=True, null=True)


class Feedback(models.Model):

    rating = models.IntegerField()
    comment = models.CharField(max_length=2048, blank=True, null=True)
    lesson_id = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

