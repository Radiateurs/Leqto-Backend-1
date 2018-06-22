from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# User Creation (POST)
# /user/create/

class UserCreate(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Details (GET, PATCH)
# /user/details/

# Need to first /user/connect/ to get the JWT Token
# Do request with Token

class UserDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# TODO : Requests to fill

# Public User Details (GET)
# /user/public/{id_user}


# Public User Search (GET)
# /user/public/search/{search_text}
