from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('login/', views.Login.as_view({'get': 'list'}), name='lg')
]
