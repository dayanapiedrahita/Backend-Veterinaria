from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions import NotFoundException, BadRequestException, ConflictException


def register_exception_handlers(app):

    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=404,
            content={"error": exc.detail}
        )

    @app.exception_handler(BadRequestException)
    async def bad_request_handler(request: Request, exc: BadRequestException):
        return JSONResponse(
            status_code=400,
            content={"error": exc.detail}
        )

    @app.exception_handler(ConflictException)
    async def conflict_handler(request: Request, exc: ConflictException):
        return JSONResponse(
            status_code=409,
            content={"error": exc.detail}
        )