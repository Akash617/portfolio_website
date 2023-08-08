from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter_email/', views.enter_email, name="Enter Email"),
]
