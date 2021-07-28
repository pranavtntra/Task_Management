from django.urls import path
from .views import UserDetails, AddUser

urlpatterns = [
    path('userdetails/', UserDetails.as_view(), name='userdetails'),
    path('createuser/', AddUser.as_view(), name='createuser'),
]