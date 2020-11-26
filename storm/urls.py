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
    path('inventory_home/', views.inventory_home, name='inventory_home'),
    path('person_home/<int:person_pk>', views.person_home, name='person_home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),

    #add
    path('add_person/', views.add_person, name='add_person'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),

    #delete
    path('storm/<int:snack_pk>/delete_inventory', views.delete_inventory, name='delete_inventory'),
    path('storm/<int:person_pk>/delete_person', views.delete_person, name='delete_person'),

    #edits
    path('edit_inventory/<int:snack_pk>', views.edit_inventory, name='edit_inventory'),
    path('person_list/', views.person_list, name='person_list'),
    path('edit_person/<int:person_pk>', views.edit_person, name='edit_person'),
    path('inventory_list/', views.inventory_list, name='inventory_list'),

    #Funcions
    path('subtract_inventory/<int:person_pk>/<int:snack_pk>', views.subtract_inventory, name='subtract_inventory'),


    #Search
]
