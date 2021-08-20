"""Hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from hello_world_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/',views.name),
    path('designation/',views.designation),
    path('Fake/',views.fake_api),
    path('Post/',views.arr_func),
    path('Response/',views.url_resp),
    path('add-data/',views.add_user_detail),
    path('Post_OP/',views.Post_operation),
    path('Total_deaths/',views.get_Total_death),
    path('Countries/',views.get_name_of_countries),
]
