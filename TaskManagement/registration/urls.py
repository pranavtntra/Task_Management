from django.urls import path
from registration.views import Dashboard, Home

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
