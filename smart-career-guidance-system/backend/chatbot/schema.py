from pydantic import BaseModel

class chatbotRequest(BaseModel):
    query:str