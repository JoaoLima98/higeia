from django.urls import path
from . import views

urlpatterns = [
    path('wings/', views.wings, name='wings'),
    path('wings/add_wing/', views.add_wing, name='add_wing'),
]