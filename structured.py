from google import genai
from pydantic import BaseModel
import enum

class Grade(enum.Enum):
    A_PLUS="a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    

class Recipe(BaseModel):
    recipe_name:str
    ingredients:list[str]
    rating: Grade


client=genai.Client()

prompt ="List a few popular cookie recipies,and include the amount of ingredients. "

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe]
    }
)

print(response.text) 