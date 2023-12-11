from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('courts/', views.courts, name='courts'),
    path('courts/details/<int:id>', views.court_details, name='court_details'),
    path('testing/', views.testing, name='testing'),
]