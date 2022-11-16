from django.urls import path
from addbank import views


urlpatterns = [
   
    path('', views.bank),
]
