# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.project import views 

urlpatterns = [


    ########################
    # OPENAI
    ########################
    path('', views.openai_home, name='openai_page'),
    path('projects/openai/', views.openai_Web, name='openai_Web'),
    
    
    
    ########################
    # WEATHER
    ########################
    path('projects/weather/', views.weather_home, name='weather_home'),
    
    # API
    path('projects/weather/API/storm', views.StormResponse, name='StormResponse'),


   
    


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
