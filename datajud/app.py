from fastapi import FastAPI
from datajud.config import Settings
from datajud.routers import predict, import_process
from alembic.config import Config
from alembic import command

settings = Settings()
app = FastAPI()

app.include_router(predict.router)
app.include_router(import_process.router)

@app.on_event("startup")
async def startup_event():  
    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(f"Error during Alembic migration: {e}")
