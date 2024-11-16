from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')                     # Enable search by title and author
    list_filter = ('publication_year',)                     # Filter by publication year

# Admin configuration for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to display in the admin list view
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    # Fields to display in the admin detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile_photo', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    # Fields for the add user form in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'profile_photo', 'date_of_birth', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
