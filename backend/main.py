from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

# from api.db.database import engine, get_db, Base

app = FastAPI(
    title="VitaCyte Inventory Application API",
    version="0.1.0",
    description="Page routing and database querying"
)

@app.get("/")
def read_root():
    return {"Hello world": "foo bar"}

@app.get("/foo-bar")
def spam_eggs():
    return {"Your": "Mother"}
