from fastapi import FastAPI
from datajud.config import Settings
from datajud.routers import predict, import_process
from alembic.config import Config
from alembic import command
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



settings = Settings()
app = FastAPI()

origins = [
    "http://127.0.0.1:8090",  
    "http://127.0.0.1:8000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/mkdocs', StaticFiles(directory='site', html=True), name='mkdocs')

app.include_router(predict.router)
app.include_router(import_process.router)

@app.on_event("startup")
async def startup_event():  
    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(f"Error during Alembic migration: {e}")
