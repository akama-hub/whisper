from django.urls import path
from django.contrib import admin
from minutes_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.file_upload, name='file_upload'),
    path('success/url', views.success_url, name='success'),
]