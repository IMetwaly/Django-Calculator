"""Calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.http import request
from django.shortcuts import render
from django.urls import path
from sum import views
from sum.views import ajax_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("calc/", views.clearer), 
    path('1/', views.one),
    path('2/', views.two),
    path('3/', views.three),
    path('4/', views.four),
    path('5/', views.five),
    path('6/', views.six),
    path('7/', views.seven),
    path('8/', views.eight),
    path('9/', views.nine),
    path('0/', views.zero),
    path('+/', views.plus),
    path('-/', views.minus),
    path('//', views.divide),
    path('x/', views.times),
    path('dot/', views.decimal),
    path('=/', views.equals),
    path('ob/', views.ob),
    path('cb/',views.cb),
    path('del/', views.Del),
    path('hey/', views.hey),
    path("",views.clearer),
    path('ajax/', views.ajax_view)
]
