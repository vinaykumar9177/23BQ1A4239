from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Vehicle Maintenance Scheduler"
)

app.include_router(router)