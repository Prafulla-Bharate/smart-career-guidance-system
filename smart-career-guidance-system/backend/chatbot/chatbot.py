from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model='models/gemini-1.5-flash-latest',temperature=0.7)

memory=ConversationBufferMemory()

chat_chain=ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False,
    prompt=PromptTemplate.from_template(
        "You are a helpful AI assistant helping students with career advice and queries.\n\n{history}\nHuman: {input}\nAI:"
    )
)

def get_bot_response(user_input:str):
    return chat_chain.run(user_input)