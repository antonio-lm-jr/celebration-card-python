from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI

from src.api.endpoints.celebration import router as celebration_router
from src.api.endpoints.health_check import router as healthcheck_router
from src.containers import Adapters, UseCases


def get_application(container: DeclarativeContainer = None) -> FastAPI:
    if container is None:
        container = UseCases(adapters=Adapters())

    container.wire(modules=["src.api.endpoints.celebration"])

    application = FastAPI()

    application.container = container
    application.include_router(celebration_router)
    application.include_router(healthcheck_router)
    return application


app = get_application()
