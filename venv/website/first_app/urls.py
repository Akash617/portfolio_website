from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('enter_email/', views.enter_email, name="enter_email"),
]
