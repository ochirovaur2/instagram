from django.urls import path
from . import views 

urlpatterns = [
    path('v1/get_followers/', views.get_followers, name='get_followers'),
    path('v1/get_list_of_unfollowing_users/', views.get_list_of_unfollowing_users, name='get_list_of_unfollowing_users'),
    
]
