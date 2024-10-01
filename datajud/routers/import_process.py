from fastapi import APIRouter
from datajud.controllers.import_process import ImportProcessController
from datajud.database import engine

router = APIRouter(prefix="/import", tags=["import"])

@router.post("/csv")
async def import_csv():
    import_controller = ImportProcessController(engine)
    return import_controller.import_process_csv()

@router.post("/api")
async def import_from_api(data: dict):
    import_controller = ImportProcessController(engine)
    return import_controller.import_process_api(data)
