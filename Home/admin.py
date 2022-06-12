from re import template
from django.contrib import admin
from django.urls import path

from django.shortcuts import render
import requests
from django.template.response import TemplateResponse


class MyAdminSite(admin.ModelAdmin):
    class Media:
        css = {
            "all":("styles.css",)

        }
        js = ("scripts.js")