from fastapi import FastAPI
from pydantic import BaseModel
from app.interact_api import interact_route
from app.extract_api import extract_data
import asyncio
import sys

# Enable proper event loop policy for Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

app = FastAPI()

class CommandInput(BaseModel):
    command: str

@app.post("/interact")
async def interact_api(input: CommandInput):
    return await interact_route(input.command)

@app.get("/extract")
async def extract_api():
    return await extract_data()
