import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def save_chunk(name: str, data: bytes):
    with open(f"{DATA_DIR}/{name}", "wb") as f:
        f.write(data)
