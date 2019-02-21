from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.tt_cup),
    url(r'^push', views.push),

]