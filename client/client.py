import requests

METADATA = "http://localhost:8000"

def upload(path):
    with open(path, "rb") as f:
        r = requests.post(f"{METADATA}/upload", files={"file": f})
    print(r.json())

upload("test.txt")
