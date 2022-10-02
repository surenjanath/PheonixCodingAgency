# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.group_project import views 

urlpatterns = [

    # The home page
    path('', views.payroll_home, name='openai_page'),
    

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
