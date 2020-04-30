"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.urls import path
from app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'),
    url(r'^produto/', views.produto, name='produto'),
    url(r'^$', views.home, name='produto'),
    url(r'^list/', views.list_produto, name='list_produto'),
    url(r'^new_produto/', views.new_produto, name='new_produto'),
    url(r'^delete_produto/', views.delete_produto, name='delete_produto'),
    url(r'^update_produto/', views.update_produto, name='update_produto'),
]
