from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .models import CustomUser


# User Registration View
@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'token': user.token, 'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login View
@api_view(['POST'])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Follow a user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


# Unfollow a user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow == request.user:
        return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)


# List users being followed by the authenticated user
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_following(request):
    following_users = request.user.following.all()
    serializer = UserSerializer(following_users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# List followers of the authenticated user
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_followers(request):
    followers = request.user.followers.all()
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
