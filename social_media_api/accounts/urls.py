from django.urls import path
from .views import (
    register_user, 
    login_user, 
    follow_user, 
    unfollow_user, 
    list_followers, 
    list_following
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('followers/', list_followers, name='list-followers'),
    path('following/', list_following, name='list-following'),
]
