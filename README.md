# User Authentication API

## About the Project

This project is developed as **Task 2 – User Authentication API** during my Backend Development Internship at **InfozaTech**.

The project implements a secure user authentication system using Python and Django REST Framework. It provides APIs for user registration, login, JWT-based authentication, protected routes, token refreshing, and logout functionality.

## Features

- User Registration API
- User Login API
- Secure Password Hashing
- JWT Access Token Generation
- JWT Refresh Token Generation
- Protected User Profile API
- Refresh Token Functionality
- User Logout API
- Refresh Token Blacklisting
- API Testing using Postman

## Technologies Used

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite
- Postman

## Project Structure

```text
User-Authentication-API/
│
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── authentication/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/user/register/` | Register a new user |
| POST | `/api/user/login/` | Login user |
| GET | `/api/user/profile/` | Get authenticated user profile |
| POST | `/api/user/token/refresh/` | Generate a new access token |
| POST | `/api/user/logout/` | Logout user and blacklist refresh token |


## Authentication Flow

1. User registers with email, name, and password.
2. Password is securely hashed before database storage.
3. User logs in using email and password.
4. JWT access and refresh tokens are generated.
5. Access token is used to access protected endpoints.
6. Refresh token generates a new access token.
7. During logout, the refresh token is blacklisted.

## API Testing

All API endpoints were tested using **Postman**.

Testing includes:
- User registration and login.
- JWT token generation.
- Accessing protected profile endpoints.
- Refreshing access tokens.
- Logging out and invalidating refresh tokens.

## Learning Outcomes

Through this project, I gained practical experience in:

- Building REST APIs using Django REST Framework.
- Implementing custom user authentication.
- Secure password management.
- JWT-based authentication and authorization.
- Protecting API endpoints.
- Managing access and refresh tokens.
- Testing APIs using Postman.

## Internship

**Organization:** InfozaTech  
**Program:** Backend Development Internship  
**Task:** Task 2 – User Authentication API

## Author

**Shardendu Prakash Gupta**

---

If you find this project useful, feel free to explore the repository!
