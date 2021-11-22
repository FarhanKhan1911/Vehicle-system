from django.urls import path
from .views import *

urlpatterns = [
    path('',vehicleListView.as_view(),name='vehicle-list'),
    path('create/',vehicleCreateView.as_view(),name='vehicle-create'),
    path('<int:pk>/',vehicleDetailView.as_view(),name='vehicle-detail'),
    path('<int:pk>/update/',vehicleUpdateView.as_view(),name='vehicle-update'),
    path('delete/<int:pk>/update/',vehicleDeleteView.as_view(),name='vehicle-delete'),
]