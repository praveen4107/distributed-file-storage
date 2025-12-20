from fastapi import FastAPI, UploadFile, File
from .storage import save_chunk

app = FastAPI(title="Storage Node")

@app.post("/store")
async def store(file: UploadFile = File(...)):
    content = await file.read()
    save_chunk(file.filename, content)
    return {"status": "stored"}
