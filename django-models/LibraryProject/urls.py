from django.contrib import admin
from django.urls import path, include  # Include function is imported here

urlpatterns = [
    path('admin/', admin.site.urls),  # This is the admin panel URL
    path('books/', include('relationship_app.urls')),  # This includes the URLs from relationship_app
]
