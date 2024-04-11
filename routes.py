from fastapi import UploadFile, APIRouter, HTTPException, Depends
from dependency import get_session
from models import User, RegistrationResponse
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import RedirectResponse
from typing import Annotated
import uuid

users = APIRouter()

IMAGEDIR ='./uploaded_images/'

@users.get('/')
async def root():
    return RedirectResponse('/docs')

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
        photo_ext = profile_picture.filename.split('.')[-1]
        if photo_ext not in ["jpg", "jpeg", "png", "svg"]:
            return {"error": "Invalid Format"}
        profile_picture.filename = f"{uuid.uuid4()}.{photo_ext}"
        with open(f"{IMAGEDIR}{profile_picture.filename}", "wb") as buffer:
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