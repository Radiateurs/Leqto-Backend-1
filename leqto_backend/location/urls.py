from django.conf.urls import url
from . import views

urlpatterns = [

    # /location/create/
    url(r'^create/', views.LocationCreate.as_view()),

]
