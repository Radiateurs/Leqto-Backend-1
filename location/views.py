from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .models import Location
from .serializers import LocationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Location Creation (POST)
# /location/create/

class LocationCreate(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Location Details (GET, PATCH)
# /location/{location_id}/

class LocationDetail(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, location_id):
        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location with location_id {' + str(location_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(location)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, location_id):
        try:
            user = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location with location_id {' + str(location_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
