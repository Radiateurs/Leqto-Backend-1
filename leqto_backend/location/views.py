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
