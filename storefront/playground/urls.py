from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('hellohtml/', views.echo_hello),
    path('helloname/',views.echo_name)
]