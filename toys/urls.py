from django.urls import path
from . import views

urlpatterns = [
    path('create-toy/', views.ToyAPIView.as_view()),
    path('read-toy/', views.ToyAPIView.as_view()),
    path('update-toy/<pk>/', views.ToyAPIView.as_view()),
    path('delete-toy/<pk>/', views.ToyAPIView.as_view()),
]
