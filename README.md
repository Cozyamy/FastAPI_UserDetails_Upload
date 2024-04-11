Certainly! Here's a basic README.md for your FastAPI application:

---

# FastAPI Application

This is a FastAPI application for managing user registration and retrieval. It allows users to register with their basic information along with a profile picture and retrieve user details by their ID.

## Setup

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cozyamy/FastAPI_UserDetails_Upload.git
   ```

2. Install the dependencies:

   ```bash
   poetry shell
   ```
   ```bash
   poetry install
   ```

### Running the Application

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will start on `http://127.0.0.1:8000`.

## API Documentation

Access the API documentation by navigating to `/docs` or `/redoc` after running the application.

### Endpoints

#### Register User

- **Method:** POST
- **URL:** `/register`
- **Description:** Register a new user with basic information and a profile picture.
- **Parameters:**
  - `name` (str): The user's name.
  - `age` (int): The user's age.
  - `gender` (str): The user's gender.
  - `ismarried` (bool): The user's marital status.
  - `profile_picture` (file): The user's profile picture.
- **Response:** Returns a message along with the newly created user.
- **Errors:** HTTP 400 if a user with the same name already exists.

#### Get User by ID

- **Method:** GET
- **URL:** `/users/{user_id}`
- **Description:** Retrieve a user by their ID from the database.
- **Parameters:**
  - `user_id` (int): The ID of the user to retrieve.
- **Response:** Returns the user object corresponding to the user ID.
- **Errors:** HTTP 404 if the user is not found.

## Usage

1. Register a new user by making a POST request to `/register`.
2. Retrieve a user by their ID using a GET request to `/users/{user_id}`.
