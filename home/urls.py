from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.sign_in),
    path('logout/', views.sign_out),
    path('secret/', views.secret),
    path('ajax/', views.ajax),
]
