from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document, Link


class User(Document):
	email: EmailStr
	password: str
	Events: Optional[List[Link[Event]]]

	class Settings:
		name = "users"

	class Config:
		schema_extra = {
						"example" : {
									"email": 1,
									"password": "FastAPI Book Launch",
									"Events": "https://linktomyimage.com/image.png",
									"description": "We will be discussingthe contents of the FastAPI book in \
													this event. Ensure to come with your own copy to win gifts!",
									"tags": ["python", "fastapi", "book", "launch"],
									"location": "Google Meet"
								}
						}

class TokenResponse(BaseModel):
	access_token: str
	token_type: str

	class Config:
		schema_extra = {
			"example": {
				"access_token": "Huge hash",
				"token_type": "Bearer"
			}
		}
