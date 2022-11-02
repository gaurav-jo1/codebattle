from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetAdvocates, name='GetAdvocates'),
    path('<str:userid>/', views.GetAdvocateDetail, name='GetAdvocateDetail'),
]
