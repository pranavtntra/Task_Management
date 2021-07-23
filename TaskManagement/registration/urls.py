from django.urls import path
from registration.views import Dashboard


urlpatterns = [

    path('', Dashboard.as_view(), name='dashboard'),
]
