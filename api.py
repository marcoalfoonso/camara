from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os

app = FastAPI()

IMAGE_PATH = "images/latest.jpg"

@app.get("/latest")
def get_latest():
    return FileResponse(IMAGE_PATH, media_type="image/jpeg")


@app.post("/upload")
async def upload_image(request: Request):
    data = await request.body()

    with open("images/latest.jpg", "wb") as f:
        f.write(data)

    return {"status": "saved"}