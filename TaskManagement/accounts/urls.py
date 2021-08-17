from accounts.models import User
from django.urls import path
from .views import UserDetails, AddUser, UserProfile, SearchUser, DeleteUser, UpdateUser

urlpatterns = [
    path('userdetails/', UserDetails.as_view(), name='userdetails'),
    path('createuser/', AddUser.as_view(), name='createuser'),
    path('userprofile/', UserProfile.as_view(), name='userprofile'),
    path('searchuser/', SearchUser.as_view(), name='searchuser'),
    path('deleteuser/<int:pk>/', DeleteUser.as_view(), name='deleteuser'),
    path('updateuser/<int:pk>/', UpdateUser.as_view(), name='updateuser'),
]
