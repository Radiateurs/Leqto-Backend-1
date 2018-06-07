from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .models import UserLeqto
from .serializers import UserLeqtoSerializer

# Create your views here.


class UserLeqtoCreate(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserLeqtoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Detail (GET, PATCH)
# /user/{user_id}/

class UserLeqtoDetail(APIView):

    def get(self, request, user_id):
        try:
            user = UserLeqto.objects.get(id=user_id)
        except UserLeqto.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserLeqtoSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        try:
            user = UserLeqto.objects.get(id=user_id)
        except UserLeqto.DoesNotExist:
            return JsonResponse({'error': 'User with user_id {' + str(user_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = UserLeqtoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
