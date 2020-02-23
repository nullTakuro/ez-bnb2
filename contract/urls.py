from django.urls import path
from contract import views
urlpatterns = [
    path('contract/', views.contract, name = 'contract'),
    path('contract-add/', views.addContract, name = 'contract-add'),
    path('property-add/', views.addProperty, name = 'property-add'),
]
