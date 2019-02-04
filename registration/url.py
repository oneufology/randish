from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view()),
    url(r'^sign_up/$', views.SignUpFormView.as_view()), #Registration
    url(r'^sign_in/$', views.SignInFormView.as_view()), #Login
    url(r'^logout/$', views.LogOutView.as_view()), #Login
]