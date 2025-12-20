from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True)

class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    chunk_name = Column(String)
    node_url = Column(String)
