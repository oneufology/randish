from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from .views import List

urlpatterns = [
    url(r'^$', List.as_view()),
    url(r'^reload', views.reload),
    # url(r'^form/$', views.form),
    # url(r'^form/add-ingredients/', views.add_ingredients),
    # url(r'^form/add-dish/$', views.add_dish),
]