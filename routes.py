from fastapi import UploadFile, APIRouter, HTTPException, Depends
from dependency import get_session
from models import User, RegistrationResponse
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from typing import Annotated

users = APIRouter()

@users.post("/register", response_model=RegistrationResponse)
async def register_user(name: str,
    age: int,
    gender: str,
    ismarried: bool,
    profile_picture: UploadFile, 
    session: Annotated[Session, Depends(get_session)]):
    """
    Register a new user

    Args:
        name (str): The user's name
        age (int): The user's age
        gender (str): The user's gender
        ismarried (bool): The user's marital status
        profile_picture (UploadFile): The user's profile picture file

    Returns:
        RegistrationResponse: A message along with the newly created user.

    Raises:
        HTTPException: If a user with the same name already exists
    """
    try:
        with open(f"./uploaded_images/{profile_picture.filename}", "wb") as buffer:
            buffer.write(profile_picture.file.read())
            user = User(name=name, age=age, gender=gender, is_married=ismarried, profile_picture=profile_picture.filename)
            session.add(user)
            session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    return RegistrationResponse(user=user)

@users.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, session: Annotated[Session, Depends(get_session)]):
    """
    A function to retrieve a user by their ID from the database.

    Parameters:
        user_id (int): The ID of the user to retrieve.
        session (Session): The database session.

    Returns:
        User: The user object corresponding to the user ID.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user