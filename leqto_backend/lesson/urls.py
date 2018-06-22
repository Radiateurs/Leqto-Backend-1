from django.conf.urls import url
from . import views

urlpatterns = [

    # /lesson/create/
    url(r'^create/', views.LessonCreate.as_view()),

    # /lesson/{lesson_id}
    url(r'^^(?P<lesson_id>[0-9]+)/', views.LessonDetail.as_view()),

]
