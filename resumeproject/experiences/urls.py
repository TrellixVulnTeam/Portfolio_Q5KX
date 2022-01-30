from django.urls import path
from . import views 

urlpatterns = [
    path('exp/', views.experience, name='exp')
]