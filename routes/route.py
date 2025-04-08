from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schemas.schemas import list_serial

router = APIRouter()


@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())