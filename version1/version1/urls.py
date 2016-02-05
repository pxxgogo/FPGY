"""version1 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'account.login.login'),
    url(r'^login$', 'account.login.login'),
    url(r'^profile$', 'account.profile.profile'),
    url(r'^changeInfo$', 'account.profile.changeInfo'),
    url(r'^changePassword$', 'account.profile.changePassword'),
    url(r'^infoChanged$', 'account.profile.infoChanged'),
    url(r'^index/$','version1.index.index'),
    url(r'^register$','account.register.register'),
    url(r'^logout$','account.logout.logout'),
    url(r'^organizationList$','organization.views.list'),
    url(r'^organization/(?P<id>\d+)/$','organization.views.organizationInfo'),
    url(r'^addNotificationTo_(?P<organizaitonID>\d+)/$','notification.views.addNotification'),
    url(r'^addActivityTo_(?P<organizaitonID>\d+)/$','activity.views.addActivity'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

