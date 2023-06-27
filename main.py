import uvicorn
from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates

from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.message import Message, MessageCreate
from app import deps
from app import crud

# Project directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent
# TEMPLATES = Jinja2Templates()

app = FastAPI()

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root(request: Request, db: Session = Depends(deps.get_db)) -> dict:
    return {"HWE": "I seem to be working correctly"}


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app")
