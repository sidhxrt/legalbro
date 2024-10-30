from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, PlainTextResponse 
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def legalquery(user_query_prompt):
    if (user_query_prompt != ""):
        parser = StrOutputParser()
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7, max_toxens=500)
        system_prompt = (
            "you are an indian legal expert. any questions asked you should be answered as if you are an indian legal advisor."
            "the user will send you a prompt, which will be a query or doubt related to law."
            "you have to give the output in such a way that you first tell the overview of situation, what are the IPCs involved and how to resolve the situation."
            "dont encourage any other questions(only indian law related questions)"
            "if you dont know answer, return 'i dont have an answer for your query'"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("user", "user_query_prompt:{input}"),   
            ]
        )


        chain = prompt | llm | parser
        return chain.invoke({"input": user_query_prompt})      

    else:
        return "you sent an empty prompt request." 

class UserInput(BaseModel):
    user_query_prompt: str | None = None
0
@app.get("/")
async def main():
    content = """
<body>
<form action="/ask" enctype="multipart/form-data" method="post">
<input name="query" type="text">
<input type="submit">
</form>
    """
    return HTMLResponse(content=content)

@app.post("/ask")
async def startfunction(query: str = Form(...)):
    response = legalquery(UserInput(query=query))
    return PlainTextResponse(content=response)
  