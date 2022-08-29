from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListCreateAPIView.as_view()),
    path('<int:pk>/', views.PhotoDestroyAPIView.as_view())
]
