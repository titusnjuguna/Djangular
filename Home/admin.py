from re import template
from urllib import response
from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from .views import my_view



class MyAdminSite(AdminSite):
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        urls += [
            path('',self.admin_view(my_view))
        ]
        return urls
    

admin_site = MyAdminSite()  
 