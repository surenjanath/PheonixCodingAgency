# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.project import views 

urlpatterns = [

    # The home page
    path('', views.openai_home, name='openai_page'),
    path('openai/Web', views.openai_Web, name='openai_Web'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
