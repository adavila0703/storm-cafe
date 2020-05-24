"""storm URL Configuration

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
from django.urls import path, include
from storm_inv import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('viewinventory/', views.viewinventory, name='viewinventory'),
    path('viewperson/<int:person_pk>', views.viewperson, name='viewperson'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),


    #add
    path('addperson/', views.addperson, name='addperson'),
    path('addinventory/', views.addinventory, name='addinventory'),

    #delete
    path('storm/<int:snack_pk>/deletesnack', views.deletesnack, name='deletesnack'),
    path('storm/<int:person_pk>/deleteperson', views.deleteperson, name='deleteperson'),

    #edits
    path('editsnack/<int:snack_pk>', views.editsnack, name='editsnack'),
    path('viewtoeditperson/', views.viewtoeditperson, name='viewtoeditperson'),
    path('editperson/<int:person_pk>', views.editperson, name='editperson'),
    path('viewtoeditinventory/', views.viewtoeditinventory, name='viewtoeditinventory'),

    #Funcions
    path('subsnack/<int:person_pk>/<int:snack_pk>', views.subsnack, name='subsnack'),


    #Search
]
