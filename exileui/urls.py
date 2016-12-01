# -*- encoding: utf8 -*-
from django.conf.urls import include, url
from exileui import views

urlpatterns = [
    url(r'^colors.css$', views.colors, name="colors"),
]
