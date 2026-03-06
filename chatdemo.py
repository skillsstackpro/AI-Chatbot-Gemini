from google import genai
from google.genai import types

client =genai.Client()

print("chat starts here....  type 'endchat' to close ")
chat =[]
userinput = input("user : ")

while userinput != 'endchat' :
    chat.append("user :" +userinput)
    systemoutput=client.models.generate_content(
        contents = chat,
        model = 'gemini-2.5-flash-lite',
        config = types.GenerateContentConfig(
            system_instruction ="Answer in 1 line within 50 characters"
        )
    )
    chat.append("statbot : " +systemoutput.text)
    print("statbot : ",systemoutput.text)
    userinput = input("user : ")