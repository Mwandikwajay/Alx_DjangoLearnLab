from django.urls import path
from .views import (
    RegisterUserView, LoginUserView, FollowUserView, 
    UnfollowUserView, ListFollowingView, ListFollowersView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('following/', ListFollowingView.as_view(), name='list-following'),
    path('followers/', ListFollowersView.as_view(), name='list-followers'),
]