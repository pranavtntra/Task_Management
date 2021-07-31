from django.urls import path
from .views import UserDetails, AddUser, UserProfile

urlpatterns = [
    path('userdetails/', UserDetails.as_view(), name='userdetails'),
    path('createuser/', AddUser.as_view(), name='createuser'),
    path('userprofile/', UserProfile.as_view(), name='userprofile')
]
