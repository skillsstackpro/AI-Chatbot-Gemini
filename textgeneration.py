from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()
# prompt = input("Enter your prompt : ")

image= Image.open("images/cat.webp")
response = client.models.generate_content_stream( 
    model ='gemini-2.5-flash',
    contents = [image, "Tell me about this image"],
    config = types.GenerateContentConfig(
        system_instruction = "response should be 1000 words, be funny",
        temperature = 0.1
    )
)
for chunk in response:
    print(chunk.text,end="---\n---")

# print("The response is ")
# print("-----------------")
# print("-----------------")
# print(response.text)