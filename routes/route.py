from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


@router.post("/")
async def create_todo(todo: Todo):
    tododict = dict(todo)
    collection_name.insert_one(tododict)
    return tododict


@router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    tododict = dict(todo)
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": tododict})
    return tododict


@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.delete_one({"_id": ObjectId(id)})
    return {"deleted": True}