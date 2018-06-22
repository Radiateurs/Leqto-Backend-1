from django.db import models

# When model changed run "$> python3 manage.py makemigrations location"
# Then "$> python3 manage.py sqlmigrate location [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "location/migrations/0001_initial.py" where migration_number = 0001
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
