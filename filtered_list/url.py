from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .views import FilteredList
from . import views

urlpatterns = [
    url(r'^$', FilteredList.as_view(), name='filtered-list'),
    url(r'^ajax/', views.ajax),
]