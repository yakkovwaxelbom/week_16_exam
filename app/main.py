from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from core.seed import load_init_data
from core.db import MongoManager
from core.handle_errors import register_error_handlers
from routes.employees_rout import router as employees_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    MongoManager.connect()
    load_init_data()
    yield 
    MongoManager.close()

app = FastAPI(lifespan=lifespan)

register_error_handlers(app)

app.include_router(employees_router, prefix='/employees', tags=['Employees'])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)