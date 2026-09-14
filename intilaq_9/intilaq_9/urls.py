import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('home.urls')),
    path('fun/',views.fun_page, name='fun_page')
]