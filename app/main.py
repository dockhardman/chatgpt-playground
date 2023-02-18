import fastapi
from fastapi.responses import PlainTextResponse

from app.config import settings


def create_app():
    app = fastapi.FastAPI()

    @app.get("/")
    async def root():
        return PlainTextResponse("OK")

    @app.on_event("startup")
    async def startup_event():
        pass

    from app.api.endpoints import router as api_router

    app.include_router(api_router, prefix=f"/api")

    return app


app = create_app()
