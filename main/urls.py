from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<str:postfix>", views.url_redirect, name="url_redirect"),
]
