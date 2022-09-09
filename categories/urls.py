from django.urls import path
from . import views

urlpatterns = [
    path('parent/', views.CategoryListCreateAPIView.as_view()),
    path('parent/<slug:slug>/', views.CategoryDetailAPIView.as_view()),
    path('parent/<int:pk>/update/', views.CategoryUpdateAPIView.as_view()),
    path('parent/<int:pk>/delete/', views.CategoryDestroyAPIView.as_view()),
    path('sub/', views.SubCategoryListCreateAPIView.as_view()),
    path('sub/<int:pk>/update/', views.SubCategoryUpdateAPIView.as_view()),
    path('sub/<int:pk>/delete/', views.SubCategoryDestroyAPIView.as_view()),
]