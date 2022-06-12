from django.contrib import admin
from django.urls import path

admin.site.site_header = "Weather admin"
admin.site.site_title = "Accuracy and Transparent"
admin.site.index_title = "Weather Update"

urlpatterns = [
    path('', admin.site.urls),

]
