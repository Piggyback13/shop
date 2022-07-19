from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user_', include('users.urls'))
]
