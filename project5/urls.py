"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HARI.views import *
from PATNAM.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HARI/',HARI,name='HARI'),
    path('HARI1/',HARI1,name='HARI'),
    path('PATNAM/',PATNAM,name='PATNAM'),
    path('PATNAM1/', PATNAM1,name='PATNAM1'),
]
