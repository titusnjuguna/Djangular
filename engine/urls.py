from django.contrib import admin
from django.urls import path
from Home.admin import admin_site

admin.site.site_header = "Weather admin"
admin.site.site_title = "Accuracy and Transparent"
admin.site.index_title = "Weather Update"

urlpatterns = [
    path('', admin_site.urls),

]
