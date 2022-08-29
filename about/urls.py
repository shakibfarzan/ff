from django.urls import path
from . import views

urlpatterns = [
    path('contact-fields/', views.ContactFieldListCreateAPIView.as_view()),
    path('contact-fields/<int:pk>/', views.ContactFieldDetailAPIView.as_view()),
    path('bio/', views.BioAPIView.as_view()),
]


