from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvocatesList.as_view(), name='GetAdvocates'),
    path('<str:userid>/', views.AdvocateDetail.as_view(), name='GetAdvocateDetail'),
]
