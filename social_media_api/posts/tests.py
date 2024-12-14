from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model  # Fetch the custom user model
from .models import Post, Comment

CustomUser = get_user_model()  # Get the CustomUser model dynamically

class PostPermissionTests(APITestCase):
    def setUp(self):
        # Create two users using the custom user model
        self.author = CustomUser.objects.create_user(username="author", password="password123")
        self.other_user = CustomUser.objects.create_user(username="otheruser", password="password123")

        # Create a post by the author
        self.post = Post.objects.create(
            author=self.author,
            title="Test Post",
            content="This is a test post."
        )

    def test_non_author_can_read_post(self):
        """Other users can read the post."""
        response = self.client.get(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_author_cannot_update_post(self):
        """Other users cannot update the post."""
        self.client.login(username="otheruser", password="password123")
        response = self.client.put(f"/api/posts/{self.post.id}/", {"title": "New Title", "content": "Updated content."})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_can_update_post(self):
        """The post author can update the post."""
        self.client.login(username="author", password="password123")
        response = self.client.put(f"/api/posts/{self.post.id}/", {"title": "Updated Title", "content": "Updated content."})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_author_cannot_delete_post(self):
        """Other users cannot delete the post."""
        self.client.login(username="otheruser", password="password123")
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_can_delete_post(self):
        """The post author can delete the post."""
        self.client.login(username="author", password="password123")
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
