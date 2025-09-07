from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
	name: str = Field(min_length=1, max_length=100)
	email: EmailStr = Field(max_length=255)

class UserRead(BaseModel):
	id: int
	name: str
	email: EmailStr


class Config:
	orm_mode = True

