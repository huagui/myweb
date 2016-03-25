"""myweb URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import login,logout

from DjangoUeditor import urls as DjangoUeditor_urls
from blog import views
# from blog.views import register, index


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login',  login, {'template_name':'blog/login.html'}),
    url(r'^register', views.register),
    url(r'^host', views.host),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^blog/(?P<host_id>\d+)/', include('blog.urls')),
    url(r'^logout',  'django.contrib.auth.views.logout_then_login'),
    # url(r'^logout/$', logout, ),
]


# use Django server /media/ files
from django.conf import settings
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(
    #     settings.STATIC_URL, document_root=settings.STATIC_ROOT)