from django.conf.urls import url
from . import views

urlpatterns = [

    # /location/create/
    url(r'^create/', views.LocationCreate.as_view()),

    # /location/{location_id}
    url(r'^^(?P<location_id>[0-9]+)/', views.LocationDetail.as_view()),
]
