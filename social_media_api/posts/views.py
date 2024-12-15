# Import the necessary modules
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters, status
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.utils import create_notification  # Import the utility for notifications

# Custom Permission: Only allow owners to edit or delete
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        """
        Override queryset to display posts from followed users if authenticated,
        otherwise display all posts.
        """
        if self.request.user.is_authenticated:
            following_users = self.request.user.following.all()
            return Post.objects.filter(author__in=following_users).order_by('-created_at')
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Automatically set the post author to the authenticated user.
        """
        serializer.save(author=self.request.user)

    # My posts endpoint
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_posts(self, request):
        """
        Retrieve posts created by the authenticated user.
        """
        queryset = Post.objects.filter(author=request.user).order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Feed endpoint
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """
        Custom action to retrieve posts from followed users.
        """
        following_users = request.user.following.all()
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Like a post
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        """
        Action to like a post and create a notification.
        """
        post = get_object_or_404(Post, pk=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(user=request.user, post=post)

        # Create a notification for the post's author
        if post.author != request.user:
            create_notification(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

    # Unlike a post
    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        """
        Action to unlike a post.
        """
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if not like.exists():
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle comment creation and management.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Create a comment and trigger a notification for the post author.
        """
        comment = serializer.save(author=self.request.user)

        # Trigger a notification for the post author
        if comment.post.author != self.request.user:  # Avoid notifying self
            create_notification(
                recipient=comment.post.author,
                actor=self.request.user,
                verb="commented on your post",
                target=comment.post
            )
