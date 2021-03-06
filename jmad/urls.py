"""jmad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from solos.views import index, solo_detail

api_patterns = [
    url(r'^', include('albums.api.urls')),
    url(r'^', include('solos.api.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$', solo_detail, name='solo_detail_view'),
    url(r'^api/', include(api_patterns, namespace='api')),
    url(r'^$', index),
]
