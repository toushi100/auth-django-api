from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', login),
    path('register', RegisterUserView.as_view(), name="register"),
    path('user', CurrentLoggedInUser.as_view(
        {'get': 'retrieve'}), name="current_user"),
]
