from motor.motor_asyncio import AsyncIOMotorClient
from models import Task
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

client=AsyncIOMotorClient("mongodb://kebyn:root@monguito:27017")
database=client.taskdatabase

colection=database.tasks

task_route=APIRouter()



@task_route.get("/api/getone/{id}")
async def get_one_task_id(id:str):
    print(id)
    oid_str = str(id)
    oid2 = ObjectId(oid_str[1:])
    print(repr(oid2))
    task = await colection.find_one({"_id":ObjectId(oid2)})
    if task:
        print("entro")
        task["_id"]=str(task["_id"])
    else:
        print('mald')

    return task

@task_route.post("/api/create")
async def create_task(task:Task):
    task_dict = task.model_dump()  
    new_task=await colection.insert_one(task_dict) 
    creted_task= await colection.find_one({'_id':new_task.inserted_id})
    if creted_task:
        creted_task['_id'] = str(creted_task['_id']) 
    return jsonable_encoder(creted_task)


@task_route.get("/api/getAll")
async def get_all_tasks():
    print("entro")
    tasks = []
    cursor = colection.find({})
    async for document in cursor:
        print(document)
        document["_id"] = str(document["_id"])  
        tasks.append(document)
    return tasks