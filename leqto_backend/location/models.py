from django.db import models

# When model changed run "$> python3 manage.py makemigrations location"
# Then "$> python3 manage.py sqlmigrate location [migration_number]"
# The migration_number is provided by the makemigrations command
# As in "location/migrations/0001_initial.py" where migration_number = 0001
# And finally run "$> python3 manage.py migrate"


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return str(self.name)


class City(models.Model):

    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Location(models.Model):

    longitude = models.FloatField()
    latitude = models.FloatField()

    street = models.CharField(max_length=256)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
