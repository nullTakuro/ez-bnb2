from django.urls import path
from calendar import views

urlpatterns = [
    path('calendar/', views.calendar, name = 'calendar'),
]
