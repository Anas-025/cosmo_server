from django.urls import path

from . import views

urlpatterns = [
    path("getUser", views.getUser, name="getUser"),
]