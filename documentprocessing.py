from google import genai
from google.genai import types
import httpx,pathlib,io

client=genai.Client()

# doc_url = "https://oup.com.pk/media/teaching-guides/Secondary%20History%20for%20Pakistan/Secondary-History-TG-6.pdf"
# doc_data=httpx.get(doc_url).content
prompt = "summarize the document"

# filepath = pathlib.Path('pdfs/bigdata.pdf')
# doc_data = filepath.read_bytes()
# pdf=types.Part.from_bytes(     
#     data= doc_data,
#     mime_type="application/pdf"
# )


long_context_pdf_path="https://oup.com.pk/media/teaching-guides/Secondary%20History%20for%20Pakistan/Secondary-History-TG-6.pdf"
doc_data=io.BytesIO(httpx.get(long_context_pdf_path).content)

pdf=client.files.upload(
    file=doc_data,
    config={
        "mime_type": "application/pdf"
    }
)

response=client.models.generate_content(
    model = "gemini-2.5-flash",
    contents =[pdf,prompt],
    config=types.GenerateContentConfig(
        system_instruction= "Answer within 200 characters "
    )
)
print(response.text)