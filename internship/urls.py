from django.urls import path
from .import views


urlpatterns = [
    
    
    path('', views.mail_list_view, name='mail_list'),
    path('mail/<int:pk>/', views.mail_detail_view, name='mail_detail'),
]