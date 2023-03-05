from fastapi import FastAPI

from src.api.endpoints.celebration import router as celebration_router
from src.api.endpoints.health_check import router as healthcheck_router
from src.containers import Adapters, UseCases


def get_application() -> FastAPI:
    container = UseCases(adapters=Adapters())

    container.wire(modules=["src.api.endpoints.celebration"])

    application = FastAPI()

    application.include_router(celebration_router)
    application.include_router(healthcheck_router)

    return application
