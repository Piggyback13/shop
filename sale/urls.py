from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale, name='sale'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.SaleDetailView.as_view(), name='sale-details'),
    path('<int:pk>/update', views.update, name='sale-update')
]
