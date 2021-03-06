"""homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# from django.contrib.auth.views import login,logout

urlpatterns = [

    # url(r'^(?P<pk>\d+)$', 'blog.views.home'),
    url(r'^$', 'blog.views.home'),
    url(r'^list$', 'blog.views.list'),
    url(r'^detail/(?P<pk>\d+)$', 'blog.views.detail'),
    url(r'^add$','blog.views.add'),
    url(r'^msg$','blog.views.msg'),
    url(r'^friend$','blog.views.friend'),
    url(r'^photo$','blog.views.photo'),
    url(r'^upload_photo$','blog.views.upload_photo'),
    url(r'^video$','blog.views.video'),
    url(r'upload_video$','blog.views.video'),
    url(r'^pro$','blog.views.pro'),
]
