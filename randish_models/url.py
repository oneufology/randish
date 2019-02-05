from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from .views import List

urlpatterns = [
    url(r'^$', List.as_view()),
    url(r'^reload', views.reload),
]