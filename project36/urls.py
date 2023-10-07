"""
URL configuration for project36 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp/',temp.as_view(),name='temp'),
    
    path('temp_by_url/',TemplateView.as_view(template_name='temp_by_url.html'),name='temp_by_url'),

    path('student_insert_form/',student_insert_form.as_view(),name='student_insert_form'),

    path('display_student/',display_student.as_view(),name='display_student'),
]
