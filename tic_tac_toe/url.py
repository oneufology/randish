from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.main),
url(r'^toe-ajax/', views.toe_ajax),
]