from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck", status_code=HTTPStatus.OK)
def health_check():
    return {"healthcheck": "ok"}
