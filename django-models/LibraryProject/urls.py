from django.contrib import admin
from django.urls import path, include  # Ensure to include the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Ensure no extra 'books/' prefix here
]
