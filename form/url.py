from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.form),
    url(r'^add-ingredients/', views.add_ingredients),
    url(r'^add-dish/', views.add_dish),
    url(r'^test/', views.test),
]