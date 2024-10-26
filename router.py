from fastapi import  Depends, APIRouter

from typing import Annotated

from repository import TasksRepository

from shemes import STaskAdd, STask , STaskId


router=APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd,Depends()],
    
    
)-> STaskId:
    task_id=await TasksRepository.add_one(task)
    return {"ok":True, "task_id":task_id}



@router.get("/tasks")
async def get_tasks() -> list[STask]:
    tasks= await TasksRepository.find_all()
    return {"data":tasks}