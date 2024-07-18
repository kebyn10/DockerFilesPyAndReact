from fastapi import FastAPI
from database import task_route
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


from fastapi import FastAPI
from database import task_route
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:5173",
    "http://frontPrueba:3000",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_route)
