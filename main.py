from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, PlainTextResponse 
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def legalquery(user_query_prompt: str):
    if user_query_prompt:
        parser = StrOutputParser()
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7, max_tokens=500)
        system_prompt = (
            "You are an Indian legal expert. Any questions asked should be answered as if you are an Indian legal advisor. "
            "The user will send you a prompt, which will be a query or doubt related to law. "
            "Provide the output by first explaining the situation, detailing the relevant IPC sections, and suggesting ways to resolve it. "
            "Don't entertain unrelated questions. If you don’t know the answer, respond with 'I don't have an answer for your query'."
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("user", user_query_prompt),  
            ]
        )

        chain = prompt | llm | parser
        return chain.invoke({"input": user_query_prompt})
    else:
        return "You sent an empty prompt request."

class UserInput(BaseModel):
    user_query_prompt: str | None = None

@app.get("/")
async def main():
    content = """
<body>
<form action="/ask" enctype="multipart/form-data" method="post">
<input name="query" type="text">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/ask")
async def startfunction(query: str = Form(...)):
    response = legalquery(query)  
    return PlainTextResponse(content=response)
