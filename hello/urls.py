# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:54:09 2020

@author: kklem
"""
from django.conf.urls import url
from .views import HelloView

urlpatterns = [
    url(r'', HelloView.as_view(), name='index'),
    
    # path('', views.index, name='index'),
    # path('next', views.next, name='next'),
    # path('form', views.form, name='form'),
    #path('<int:id>/<nickname>/', views.index, name='index'),
    
]

