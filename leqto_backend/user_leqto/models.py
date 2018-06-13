from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


# When model changed run "$> python3 manage.py makemigrations user_leqto"
# Then "$> python3 manage.py sqlmigrate user_leqto [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "user_leqto/migrations/0001_initial.py" where migration_number = 0001
# And finally run "$> python3 manage.py migrate"


class User(BaseUser):

    # null=True makes the field optional in the database
    # blank=True makes the field optional when adding creating it with admin panel

    date_of_birth = models.DateField(blank=True, null=True)
    facebook_link = models.CharField(max_length=256, blank=True, null=True)
    google_link = models.CharField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=256, blank=True, null=True)
    payment_info = models.IntegerField(blank=True, null=True)

    objects = BaseUserManager()

