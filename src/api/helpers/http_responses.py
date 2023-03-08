from typing import Any


def ok(data: Any) -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "status_code": 200,
        "content": data,
    }

    return parsed


def created(data: Any) -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "status_code": 201,
        "content": data,
    }

    return parsed


def bad_request(data: Any) -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "status_code": 400,
        "content": {"status_code": data.status_code, "message": data.message},
    }

    return parsed


def internal_server_error() -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "status_code": 500,
        "content": {
            "status_code": "internal_error",
            "message": "Internal Server Error",
        },
    }

    return parsed


def not_found(data: Any) -> dict[str, Any]:
    parsed: dict[str, Any] = {
        "status_code": 404,
        "content": {"status_code": data.status_code, "message": data.message},
    }

    return parsed
