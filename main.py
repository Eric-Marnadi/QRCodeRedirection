from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os

app = FastAPI()

class Msg(BaseModel):
    msg: str



@app.get("/")
async def root():
    f = open("link.txt", "r")
    link = f.read()
    f.close()
    return RedirectResponse(link)


@app.post("/change_link/{token}")
async def change_link(token: str, msg: Msg):
    if token == os.environ.get('LINK_TOKEN'):
        f = open("link.txt", "w")
        f.write(msg.msg)
        f.close()
        return {"message": "Was able to change link"}
    return {"message": "Token was wrong"}

@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}