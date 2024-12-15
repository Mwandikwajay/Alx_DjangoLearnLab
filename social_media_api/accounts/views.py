from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserSerializer
)

# User Registration View
class RegisterUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.serializer_class.Meta.model.objects.get(username=response.data['username'])
        return Response({'token': user.token, 'username': user.username}, status=status.HTTP_201_CREATED)


# User Login View
class LoginUserView(CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Follow a User
class FollowUserView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


# Unfollow a User
class UnfollowUserView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user_to_unfollow = self.get_object()
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)


# List Users Being Followed
class ListFollowingView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()


# List Followers
class ListFollowersView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()
