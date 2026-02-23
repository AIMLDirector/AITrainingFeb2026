from pydantic import BaseModel, EmailStr, Field
from typing import List 

class User(BaseModel):
    id: int = Field (gt =10 , lt = 100)
    name: str
    email: EmailStr
    role: str = Field(default="user", List[str] = ["user", "admin"])

user_input  = User(id=50, name=10, email="kumar")

print(user_input)   