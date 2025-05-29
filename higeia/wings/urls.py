from django.urls import path
from . import views

urlpatterns = [
    path('wings/', views.wings, name='wings'),
    path('wings/delete/<str:code>', views.delete, name='delete'),
    path('wings/add_wing/', views.add_wing, name='add_wing'),
    path('wings/update/<str:code>/', views.update, name='update'),
]