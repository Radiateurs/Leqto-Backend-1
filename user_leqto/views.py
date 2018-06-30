from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
import json
from django.db.models import Q

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
# or /user/details/?user={id_user}

# With param retrieve User information from its id.
# No need of token first

# Without param
# Need to first /user/connect/ to get the JWT Token
# Do request with Token

class UserDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_request = request.GET.get('user', None)

        # get the id to look for
        if user_request is not None:
            user_id = user_request
        else:
            user_id = request.user.id

        # get user object
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(request.user.id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class UserSearch(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = request.GET.get('query', None)
        if query is None:
            return JsonResponse({'error': 'No query found'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_firstname = list(User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)))
        except User.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        response = json.loads('[]')
        for value in user_firstname:
            serializer_f = UserSerializer(value, data=request.data, partial=True)
            if serializer_f.is_valid():
                serializer_f.save()
                response.append(json.loads(json.dumps(serializer_f.data)))
        print(json.dumps(response))
        if len(response) > 0:
            return JsonResponse(response, status=status.HTTP_200_OK, safe=False)
        return JsonResponse({'error': 'test'}, status=status.HTTP_404_NOT_FOUND)
