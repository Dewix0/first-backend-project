from database import new_session
from shemes import STaskAdd
from database import TaskOrm
from sqlalchemy import select
from shemes import STask


class TasksRepository:
    @classmethod
    
    async def add_one(cls,data:STaskAdd):
        async with new_session() as session:
            task_dict=data.model_dump()
            
            task=TaskOrm(**task_dict)
            
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
            
        
    @classmethod
    
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result= await session.execute(query)
            task_models=result.scalars().all()
            task_shemes = [STask.model_validate(task_model) for task_model in task_models]
            return task_models