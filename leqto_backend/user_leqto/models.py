from django.db import models
from django.contrib.auth.models import AbstractUser

# When model changed run "$> python3 manage.py makemigrations user_leqto"
# Then "$> python3 manage.py sqlmigrate user_leqto [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "user_leqto/migrations/0001_initial.py" where migration_number = 0001
# And finally run "$> python3 manager.py migrate"


class UserLeqto(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    facebook_link = models.CharField(max_length=256, blank=True, null=True)
    google_link = models.CharField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=256, blank=True, null=True)
    payment_info = models.IntegerField(blank=True, null=True)

