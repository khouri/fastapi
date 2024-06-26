from pydantic import BaseModel
from typing import List


class Event(BaseModel):
	id: int
	title: str
	image: str
	description: str
	tags: List[str]
	location: str

	class Config:
		schema_extra = {
						"example" : {
									"id": 1,
									"title": "FastAPI Book Launch",
									"image": "https://linktomyimage.com/image.png",
									"description": "We will be discussingthe contents of the FastAPI book in \
													this event. Ensure to come with your own copy to win gifts!",
									"tags": ["python", "fastapi", "book", "launch"],
									"location": "Google Meet"
								}
						}
