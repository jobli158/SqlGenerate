"""djangoProject URL Configuration

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
from django.contrib.sites import admin
from django.urls import path, include



from djangoProject.view import *

urlpatterns = [
    path('', index.as_view(),name='index'),
    path('download',download.as_view(),name='download'),
    path('save',save.as_view(),name='save'),
    path('look',look.as_view(),name='look'),
    path('createtable',createtable.as_view(), name='createtable'),
    path('savetable',savetable.as_view(), name='savetable'),
    path('savedatabase',savedatabases.as_view(), name='savedatabase'),
    path('uploadsql',upload_sql.as_view(), name='uploadsql'),
    path('uploadtable',upload_table.as_view(), name='uploadtable'),
    path('lookinfo', look_info.as_view(), name='lookinfo'),
]
