from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.api.helpers.http_responses import (
    bad_request,
    created,
    internal_server_error,
    not_found,
    ok,
)
from src.application.dtos.create_celebration_dto import CreateCelebrationDTO
from src.application.exceptions.celebration_expection import (
    CelebrationNotFoundException,
)
from src.containers import UseCases
from src.domain.exceptions.base_domain import BaseDomainException

router = APIRouter()


@router.post("/celebration")
@inject
async def create_celebration(
    celebration_input: CreateCelebrationDTO,
    use_case=Provide[UseCases.create_celebration],
):
    try:
        celebration_result = use_case.create_celebration(celebration_input)
        to_json = jsonable_encoder(celebration_result)

        return JSONResponse(
            created(to_json),
            status_code=HTTPStatus.CREATED,
        )
    except BaseDomainException as error:
        return JSONResponse(
            bad_request(error), status_code=HTTPStatus.BAD_REQUEST
        )

    except Exception as error:
        print(error)
        return JSONResponse(
            internal_server_error(),
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@router.get("/celebration/{celebration_id}")
@inject
async def get_celebration(
    celebration_id: str, use_case=Provide[UseCases.get_celebration]
):
    try:
        uc_result = use_case.get_celebration(celebration_id)
        to_json = jsonable_encoder(uc_result)

        return JSONResponse(
            ok(to_json),
            status_code=HTTPStatus.OK,
        )
    except CelebrationNotFoundException as error:
        print(error)
        return JSONResponse(
            not_found(error),
            status_code=HTTPStatus.NOT_FOUND,
        )
    except Exception:
        return JSONResponse(
            internal_server_error(),
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        )
