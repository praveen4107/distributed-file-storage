# Distributed File Storage System

**Distributed File Storage System** developed using Python and FastAPI. Files uploaded to the system are split into smaller chunks and stored across multiple storage nodes, while a metadata server maintains information about file locations.


## Features

-   File chunking and distributed storage

-   Centralized metadata management

-   Multiple storage nodes

-   REST API based communication

-   Scalable architecture

-   Docker-based deployment


## Architecture

The system follows a **microservice architecture** where metadata management and storage are handled by separate services.

```
Client
  |
  | (REST API)
  v
Metadata Server
  |
  | (REST API)
  v
Storage Nodes
```


## Components

### Client

-   Uploads files to the metadata server

### Metadata Server

-   Splits files into chunks

-   Assigns chunks to storage nodes

-   Stores metadata about files and chunk locations

### Storage Nodes

-   Receive file chunks from metadata server

-   Store chunks in local storage directories


## Tech Stack

-   Python

-   FastAPI

-   REST APIs

-   SQLite

-   SQLAlchemy

-   Docker

-   Docker Compose


## Project Structure

```
distributed-file-storage/
│
├── client/
│   └── client.py
│
├── metadata_server/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routes.py
│   │   └── utils.py
│   └── Dockerfile
│
├── storage_node/
│   ├── app/
│   │   ├── main.py
│   │   └── storage.py
│   ├── data/
│   └── Dockerfile
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```


## Setup Instructions

### Create Virtual Environment

```
python -m venv venv
```

Activate it:

```
source venv/bin/activate
# Windows: venv\Scripts\activate
```


### Install Dependencies

```
pip install -r requirements.txt
```


## Running the Project

### Start Metadata Server

```
uvicorn metadata_server.app.main:app --port 8000 --reload
```

### Start Storage Nodes (separate terminals)

```
uvicorn storage_node.app.main:app --port 8001 --reload
uvicorn storage_node.app.main:app --port 8002 --reload
```


## Docker Deployment

### Build and Run Containers

```
docker-compose up --build
```

### Stop Containers

```
docker-compose down
```
