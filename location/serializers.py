from rest_framework import serializers
from .models import Location, Country, City, ZipCode


class LocationSerializer(serializers.ModelSerializer):
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    zip_code = serializers.CharField(required=True)

    class Meta:
        model = Location
        fields = ['longitude',
                  'latitude',
                  'street',
                  'city',
                  'country',
                  'zip_code']

    def validate(self, data):

        # In case of a partial patch, will skip the validation of country/city/zip_code
        if data.get('country') is None and data.get('city') is None and data.get('zip_code') is None:
            return data

        # Check if the country_id, city_id and zip_code are all present on the data map
        # Either way raise error to explicitly inform the need of all IDs
        if not (data.get('country') is not None
                and data.get('city') is not None
                and data.get('zip_code') is not None):
            raise serializers.ValidationError('Need both country_id and city_id to update them')

        # Check if the country exists
        country_id = data.get('country')
        try:
            country = Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            raise serializers.ValidationError('Country with country_id {' + str(country_id) + '} does not exist')

        # Check if the city exists
        city_id = data.get('city')
        try:
            city = City.objects.get(id=city_id)
        except City.DoesNotExist:
            raise serializers.ValidationError('City with city_id {' + str(city_id) + '} does not exist')

        # Check if the zip_code exists
        zip_code_id = data.get('zip_code')
        try:
            zip_code = ZipCode.objects.get(id=zip_code_id)
        except Country.DoesNotExist:
            raise serializers.ValidationError('Zip code with zip_code_id {' + str(zip_code_id) + '} does not exist')

        # Check if the city.country.id is the same as the country_id
        if country.id is not city.country.id:
            raise serializers.ValidationError('City with city_id {' + str(city.id) + '} have country_id {'
                                              + str(city.country.id) + '} which is not equal to the passed country id {'
                                              + str(country.id) + '}')

        # Check if the zip_code.country.id is the same as the country_id
        if country.id is not zip_code.country.id:
            raise serializers.ValidationError('Zip code with zip_code_id {' + str(zip_code.id) + '} have country_id {'
                                              + str(zip_code.country.id) +
                                              '} which is not equal to the passed country id {' + str(country.id) + '}')

        # Check if the zip_code.city.id is the same as the city_id
        if city.id is not zip_code.city.id:
            raise serializers.ValidationError('Zip code with zip_code_id {' + str(zip_code.id) + '} have city_id {'
                                              + str(zip_code.city.id) +
                                              '} which is not equal to the passed city id {' + str(city.id) + '}')
        return data

    def create(self, validated_data):
        country_id = validated_data.pop('country', None)
        country = Country.objects.get(id=country_id)

        city_id = validated_data.pop('city', None)
        city = City.objects.get(id=city_id)

        zip_code_id = validated_data.pop('zip_code', None)
        zip_code = ZipCode.objects.get(id=zip_code_id)

        return Location.objects.create(country=country, city=city, zip_code=zip_code, **validated_data)

    def update(self, instance, validated_data):
        country_id = validated_data.pop('country', None)
        city_id = validated_data.pop('city', None)
        zip_code_id = validated_data.pop('zip_code', None)

        if city_id and country_id:
            country = Country.objects.get(id=country_id)
            validated_data['country'] = country
            city = City.objects.get(id=city_id)
            validated_data['city'] = city
            zip_code = ZipCode.objects.get(id=zip_code_id)
            validated_data['zip_code'] = zip_code

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
