from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os

app = FastAPI()
link = "https://www.youtube.com/"

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return RedirectResponse(link)


@app.post("/change_link/{token}")
async def change_link(token: str, msg: Msg):
    if token == os.environ.get('LINK_TOKEN'):
        link = msg.msg
        return {"message": "Was able to change link to " + link}
    return {"message": "Token was wrong", "token": token, "real": os.environ.get("LINK_TOKEN")}

@app.get("/link")
async def link():
    return {"link": link}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}