# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from core.views import *


urlpatterns = [
    path("", include("apps.landing.urls")), 
    path('admin/', admin.site.urls),          
    path("Login/", include("apps.authentication.urls")), 
    path("project/", include("apps.project.urls")) ,
    path("group_project/", include("apps.group_project.urls")) ,
    path("Dashboard/", include("apps.home.urls"))   ,          
    path("Dashboard/", include("apps.home.urls"))   ,  
    
    
    
    
    path("update_server/", update, name="update"),        
                
]
