from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import requests, uuid

from .database import SessionLocal
from .models import File as FileModel, Chunk
from .utils import CHUNK_SIZE

router = APIRouter()

STORAGE_NODES = [
    "http://storage1:8001",
    "http://storage2:8002"
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_entry = FileModel(filename=file.filename)
    db.add(file_entry)
    db.commit()
    db.refresh(file_entry)

    chunk_count = 0

    while True:
        chunk = await file.read(CHUNK_SIZE)
        if not chunk:
            break

        chunk_name = f"{uuid.uuid4()}.chunk"
        node = STORAGE_NODES[chunk_count % len(STORAGE_NODES)]

        requests.post(
            f"{node}/store",
            files={"file": (chunk_name, chunk)}
        )

        db.add(Chunk(
            file_id=file_entry.id,
            chunk_name=chunk_name,
            node_url=node
        ))

        chunk_count += 1

    db.commit()
    return {"filename": file.filename, "chunks": chunk_count}

@router.get("/download/{filename}")
def download_file(filename: str, db: Session = Depends(get_db)):
    file = db.query(FileModel).filter_by(filename=filename).first()
    chunks = db.query(Chunk).filter_by(file_id=file.id).all()
    return chunks
