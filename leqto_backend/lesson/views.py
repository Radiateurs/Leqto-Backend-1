from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .models import Lesson
from .serializers import LessonSerializer

from user_leqto.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Lesson Creation (POST)
# /lesson/create/

class LessonCreate(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            lesson = serializer.save()
            lesson.user_id = User.objects.get(id=request.user.id)
            lesson.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Lesson Details (GET, PATCH)
# /lesson/{lesson_id}/

class LessonDetail(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, lesson_id):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'Lesson with lesson_id {' + str(lesson_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        serializer = LessonSerializer(lesson)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, lesson_id):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return JsonResponse({'error': 'Lesson with lesson_id {' + str(lesson_id) + '} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
        if request.user == lesson.user_id:
            serializer = LessonSerializer(lesson, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'error': 'Lesson with lesson_id {' + str(lesson_id) + '} can only modified by its creator'},
                            status=status.HTTP_401_UNAUTHORIZED)

