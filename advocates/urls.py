from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvocatesList.as_view(), name='GetAdvocates'),
    # path('<int:pk>/', views.AdvocateDetail.as_view(), name='GetAdvocateDetail'),
]
