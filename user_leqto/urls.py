from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    # /user/create/
    url(r'^create/', views.UserCreate.as_view()),

    # /user/details/
    url(r'^details/', views.UserDetail.as_view()),
    url(r'^details/', views.UserDetail.as_view()),

    url(r'^search/', views.UserSearch.as_view()),


    # TODO: Update Token
    # Update token with old token
    # TODO: Automatically Delete Token
    # Automatically Delete token if new one is requested

    # /user/connect/
    url(r'^connect/', obtain_jwt_token),


]
