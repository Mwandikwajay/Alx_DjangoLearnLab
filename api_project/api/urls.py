from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import for token authentication
from .views import BookList, BookViewSet

# Instantiate the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns
urlpatterns = [
    # Route for ListAPIView
    path('books/', BookList.as_view(), name='book-list'),
    # Routes for the ViewSet (CRUD operations)
    path('', include(router.urls)),
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
