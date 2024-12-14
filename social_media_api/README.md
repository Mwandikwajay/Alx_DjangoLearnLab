Social Media API
A simple Social Media API built with Django and Django REST Framework to handle user registration, authentication, and profile management.

Project Setup
Follow these steps to set up the project on your local machine:

1.Clone the repository:
    git clone <repository-url>
    cd social_media_api
2.Set up a virtual environment:
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
3.Install dependencies:
    pip install -r requirements.txt
4.Run migrations:
    python3 manage.py makemigrations
    python3 manage.py migrate
5.Start the development server:
    python3 manage.py runserver

Endpoints
1. User Registration
URL: POST /accounts/register/
Purpose: Register a new user.
Request Body:
    json
    {
        "username": "testuser",
        "password": "password123",
        "bio": "This is my bio"
    }
Response:
json
    {
        "token": "generated_token_here",
        "username": "testuser"
    }
2. User Login
URL: POST /accounts/login/
Purpose: Authenticate an existing user and retrieve a token.
Request Body:
    json
    {
        "username": "testuser",
        "password": "password123"
    }
Response:
json
    {
        "token": "generated_token_here",
        "username": "testuser"
    }
User Model
The project uses a custom user model extending Django's AbstractUser with the following additional fields:
    bio: A short description of the user.
    profile_picture: (To be implemented later)
    followers: A ManyToMany relationship for following other users.
Authentication
This API uses Token Authentication provided by Django REST Framework:
Users receive a token upon registration or login.
Include the token in the Authorization header for protected endpoints:   
    Authorization: Token <your_token_here>
Tools Used
    Django: Web framework for Python.
    Django REST Framework: For building RESTful APIs.
    SQLite: Default database (can be replaced with PostgreSQL).


Posts Endpoints
Method	URL	Description	Authentication Required
| Endpoint           | Method | Description                      |
|--------------------|--------|----------------------------------|
| `/api/posts/`      | GET    | Retrieve all posts               |
| `/api/posts/`      | POST   | Create a new post                |
| `/api/posts/{id}/` | GET    | Retrieve a specific post by ID   |
| `/api/posts/{id}/` | PUT    | Update a post by ID              |
| `/api/posts/{id}/` | DELETE | Delete a post by ID              |

Example - Create Post
Request:
POST /api/posts/
Authorization: Token <Your-Token>
{
  "title": "Second Post",
  "content": "This is the content of the second post."
}
Response:
{
  "id": 1,
  "author": "testuser",
  "title": "Second Post",
  "content": "This is the content of the second post.",
  "created_at": "2024-12-14T10:17:07.891166Z",
  "updated_at": "2024-12-14T10:17:07.891202Z"
}

Comments Endpoints
| Endpoint                | Method | Description                             |
|-------------------------|--------|-----------------------------------------|
| `/api/comments/`        | GET    | Retrieve all comments                   |
| `/api/comments/`        | POST   | Create a new comment                    |
| `/api/comments/{id}/`   | GET    | Retrieve a specific comment by ID       |
| `/api/comments/{id}/`   | PUT    | Update a comment by ID                  |
| `/api/comments/{id}/`   | DELETE | Delete a comment by ID                  |

Example - Create Comment
Request:
POST /api/comments/
Authorization: Token <Your-Token>
{
  "post": 1,
  "content": "This is a comment on the post."
}

Response:
{
  "id": 1,
  "post": 1,
  "author": "testuser",
  "content": "This is a comment on the post.",
  "created_at": "2024-12-14T10:30:45.891166Z",
  "updated_at": "2024-12-14T10:30:45.891202Z"
}
