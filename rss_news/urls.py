from django.conf.urls import url
from django.contrib import admin
from rss_news import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'post/(?P<index>[0-9]+)$', views.post),
    url(r'login/$', views.login),
    url(r'signup/$', views.signup),
    url(r'signup_user/$', views.signup_user, name="signup_user"),
    url(r'login_user/$', views.login_user, name="login_user"),
]