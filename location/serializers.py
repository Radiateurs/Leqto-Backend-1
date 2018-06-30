from rest_framework import serializers
from .models import Location, Country, City
from operator import xor


class LocationSerializer(serializers.ModelSerializer):
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    class Meta:
        model = Location
        fields = ['longitude',
                  'latitude',
                  'street',
                  'city',
                  'country',
                  'zip_code']

    def validate(self, data):

        """
        In case of a partial patch, will skip the validation of country/city
        """
        if data.get('country') is None and data.get('city') is None:
            return data

        """
        Check if the country_id and city_id are both present on the data map
        Either way raise error to explicitly inform the need of both IDs
        """
        if xor(data.get('country') is None, data.get('city') is None):
            raise serializers.ValidationError('Need both country_id and city_id to update them')

        """
        Check if the country exists
        """
        country_id = data.get('country')
        try:
            country = Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            raise serializers.ValidationError('Country with country_id {' + str(country_id) + '} does not exist')

        """
        Check if the city exists
        """
        city_id = data.get('city')
        try:
            city = City.objects.get(id=city_id)
        except City.DoesNotExist:
            raise serializers.ValidationError('City with city_id {' + str(city_id) + '} does not exist')

        """
        Check if the city.country_id is the same as the country_id
        """
        if country.id is not city.country.id:
            raise serializers.ValidationError('City with city_id {' + str(city.id) + '} have country_id {'
                                              + str(city.country.id) + '} which is not equal to the passed country id {'
                                              + str(country.id) + '}')

        return data

    def create(self, validated_data):
        country_id = validated_data.pop('country', None)
        country = Country.objects.get(id=country_id)

        city_id = validated_data.pop('city', None)
        city = City.objects.get(id=city_id)

        return Location.objects.create(country=country, city=city, **validated_data)

    def update(self, instance, validated_data):
        country_id = validated_data.pop('country', None)
        city_id = validated_data.pop('city', None)
        if city_id and country_id:
            country = Country.objects.get(id=country_id)
            validated_data['country'] = country
            city = City.objects.get(id=city_id)
            validated_data['city'] = city

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
