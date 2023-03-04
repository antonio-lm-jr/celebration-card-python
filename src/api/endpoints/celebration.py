from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.application.dtos.create_celebration_dto import CreateCelebrationDTO
from src.application.exceptions.celebration_expection import (
    CelebrationNotFoundException,
)
from src.containers import UseCases

router = APIRouter()


@router.post("/celebration", status_code=HTTPStatus.CREATED)
@inject
async def create_celebration(
    celebration_input: CreateCelebrationDTO,
    use_case=Provide[UseCases.create_celebration],
):
    try:
        celebration_result = use_case.create_celebration(celebration_input)
        return celebration_result
    except ValidationError:
        raise HTTPException(status_code=400)
    except Exception:
        raise HTTPException(status_code=500)


@router.get("/celebration/{celebration_id}", status_code=HTTPStatus.OK)
@inject
async def get_celebration(
    celebration_id: str, use_case=Provide[UseCases.get_celebration]
):
    try:
        uc_result = use_case.get_celebration(celebration_id)
        return uc_result
    except CelebrationNotFoundException as error:
        raise HTTPException(status_code=404, detail=error.message)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)
