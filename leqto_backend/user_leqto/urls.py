from django.conf.urls import url, include
from . import views

urlpatterns = [

    # /user/create/
    url(r'^create/$', views.UserLeqtoCreate.as_view()),

    # /user/{user_id}
    url(r'^(?P<user_id>[0-9]+)/$', views.UserLeqtoDetail.as_view()),
]
