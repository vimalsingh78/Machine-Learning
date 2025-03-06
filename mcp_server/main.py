from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional, List
import uvicorn

app = FastAPI(title="MCP Server")

# Models
class Message(BaseModel):
    content: str
    timestamp: datetime = datetime.now()
    sender: str

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

# In-memory storage (replace with database in production)
messages = []
users = {}

# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = users.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Routes
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User(username=form_data.username)
    users[form_data.username] = user
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/messages", response_model=List[Message])
async def get_messages(current_user: User = Depends(get_current_user)):
    return messages

@app.post("/messages", response_model=Message)
async def create_message(
    message: Message,
    current_user: User = Depends(get_current_user)
):
    message.sender = current_user.username
    messages.append(message)
    return message

@app.get("/")
async def root():
    return {"message": "Welcome to MCP Server"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
