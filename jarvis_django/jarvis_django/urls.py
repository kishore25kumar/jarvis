"""jarvis_django URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import jarvis_django.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ping/', jarvis_django.views.elb_ping),
    url(r'^text-to-speech/', jarvis_django.views.text_to_speech),
    url(r'^demo', jarvis_django.views.demo),
    url(r'^$', jarvis_django.views.index),
]
