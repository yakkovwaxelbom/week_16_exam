from pymongo.errors import *
from fastapi import Request
from fastapi.responses import JSONResponse


def register_error_handlers(app):

    @app.exception_handler(DuplicateKeyError)
    def duplicate_key(request: Request, exc: DuplicateKeyError):
        return JSONResponse(
            status_code=400,
            content={"message": "Duplicate key", "endpoint": request.url.path}
        )

    @app.exception_handler(ServerSelectionTimeoutError)
    def mongo_timeout(request: Request, exc: ServerSelectionTimeoutError):
        return JSONResponse(
            status_code=503,
            content={"message": "MongoDB unavailable"}
        )
    
    @app.exception_handler(Exception)
    def generic_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "Internal server error"}
        )
