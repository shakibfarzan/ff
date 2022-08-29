from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view()),
    path('<slug:slug>/', views.CategoryDetailAPIView.as_view()),
    path('<int:pk>/update/', views.CategoryUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.CategoryDestroyAPIView.as_view())
]