from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class UserCreate(SQLModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the user", schema_extra={"example": "John Doe"}, title="Name")
    age: int = Field(min_length=1, max_length=3, description="Age of the user", schema_extra={"example": 30}, title="Age")
    gender: str = Field(description="Gender of the user", schema_extra={"example": "male"}, title="Gender")
    is_married: bool = Field(description="Marital status of the user", schema_extra={"example": True}, title="Marital status")
    profile_picture: str = Field(description="Profile picture of the user", schema_extra={"example": "afr.png"}, title="Profile picture")


class User(UserCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RegistrationResponse(BaseModel):
    message: str = "User registered successfully"