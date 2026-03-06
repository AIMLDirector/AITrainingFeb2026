from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class User(BaseModel):
    id: int = Field(gt=10, lt=100)
    name: str
    email: EmailStr
    role: Literal["user", "admin"] = "user"

user_input = User(
    id=50,
    name="Kumar",
    email="kumar@gmail.com"
)

print(user_input) 