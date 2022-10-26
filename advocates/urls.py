from django.urls import path

from . import views

urlpatterns = [
    path('', views.getAdvocates, name='Advocates'),
    path('<str:userid>/', views.getAdvocateDetail, name='AdvocateDetail'),
]
