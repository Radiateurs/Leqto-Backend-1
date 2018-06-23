from rest_framework import serializers
from .models import Location, Country, City


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

    def create(self, validated_data):
        city_name = validated_data.pop('city', None)
        country_name = validated_data.pop('country', None)
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            country = Country.objects.create(**validated_data)

        try:
            city = City.objects.get(name=city_name, country=country)
        except City.DoesNotExist:
            city = City.objects.create(country=country, **city_name)

        return Location.objects.create(country=country, city=city, **validated_data)

    # def update(self, instance, validated_data):
    #     city_dict = validated_data.pop('city', None)
    #     if city_dict:
    #         city_obj = instance.location
    #         for key, value in city_dict.items():
    #             setattr(city_obj, key, value)
    #             city_obj.save()
    #         validated_data['city'] = city_obj
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance


