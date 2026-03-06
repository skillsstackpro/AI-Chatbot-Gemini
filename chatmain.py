from google import genai
from google.genai import types

client =genai.Client()
chat =client.chats.create(model="gemini-2.5-flash")

print("chat starts here....  type 'endchat' to close ")

userinput = input("user : ")
while userinput != 'endchat':  
    response=chat.send_message(userinput)
    print("statbot :"+response.text)
    userinput = input("user : ")

