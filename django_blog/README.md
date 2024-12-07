Authentication Process

Registration: Users can register at /register/. Upon successful registration, they are redirected to the login page.
Login: Users can log in at /login/ and access protected pages like /profile/.
Logout: Users can log out at /logout/ using a POST request.
Profile: Users can view and update their username and email at /profile/.
Template Files

base.html: Base layout for all pages.
register.html: Template for user registration.
login.html: Template for user login.
logout.html: Template for logout confirmation.
profile.html: Template for profile management.
URLs

/: Home Page
/posts/: Blog Posts Page
/login/: Login Page
/logout/: Logout Page
/register/: Registration Page
/profile/: Profile Management Page

Authentication Process

Registration: Users can register at /register/. Upon successful registration, they are redirected to the login page.
Login: Users can log in at /login/ and access protected pages like /profile/.
Logout: Users can log out at /logout/ using a POST request.
Profile: Users can view and update their username and email at /profile/.
Template Files

base.html: Base layout for all pages.
register.html: Template for user registration.
login.html: Template for user login.
logout.html: Template for logout confirmation.
profile.html: Template for profile management.
URLs

/: Home Page
/posts/: Blog Posts Page
/login/: Login Page
/logout/: Logout Page
/register/: Registration Page
/profile/: Profile Management Page

Comment System
The comment system allows users to interact with blog posts by adding, editing, and deleting comments.

Features:
Add a Comment:

Authenticated users can leave comments on a blog post.
Comment form is available at the bottom of the post detail page.
Edit a Comment:

Comment authors can edit their own comments.
Delete a Comment:

Comment authors can delete their own comments.
Permissions:

Only logged-in users can add comments.
Only the author of a comment can edit or delete it.
Endpoints:
Add Comment: /post/<post_id>/comments/new/
Edit Comment: /comments/<comment_id>/edit/
Delete Comment: /comments/<comment_id>/delete/
How It Works:
Go to a post detail page (e.g., /post/1/).
Add a comment using the provided form.
Edit or delete your comment by clicking the respective buttons next to it.