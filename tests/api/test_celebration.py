from http import HTTPStatus

import pytest


class TestAPICelebration:
    def test_should_return_success(self, client, create_celebration_payload):
        response = client.post("/celebration", json=create_celebration_payload)
        result = response.json()

        assert response.status_code == HTTPStatus.CREATED

        assert result["status_code"] == HTTPStatus.CREATED
        assert result["content"] is not None

        assert result["content"]["id"] is not None
        assert result["content"]["created_at"] is not None
        assert result["content"]["updated_at"] is not None

        assert result["content"]["of"] == create_celebration_payload["of"]
        assert result["content"]["to"] == create_celebration_payload["to"]
        assert (
            result["content"]["description"]
            == create_celebration_payload["description"]
        )

    @pytest.mark.parametrize(
        "celebration_payload",
        [
            {"of": "", "to": "mock-to", "description": "mock-description"},
            {"of": "mock-of", "to": "", "description": "mock-description"},
            {
                "of": "m" * 2,
                "to": "mock-to",
                "description": "mock-description",
            },
            {
                "of": "mock-of",
                "to": "m" * 2,
                "description": "mock-description",
            },
            {
                "of": "m" * 101,
                "to": "mock-to",
                "description": "mock-description",
            },
            {
                "of": "mock-of",
                "to": "mock-to" * 101,
                "description": "mock-description",
            },
            {
                "of": "mock-of",
                "to": "mock-to",
                "description": "mock-description" * 401,
            },
        ],
    )
    def test_should_return_bad_request(self, client, celebration_payload):
        response = client.post("/celebration", json=celebration_payload)
        result = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST

        assert result["status_code"] == HTTPStatus.BAD_REQUEST
        assert result["content"] is not None

        assert result["content"]["status_code"] is not None
        assert result["content"]["message"] is not None

    def test_should_return_not_exists(self, client):
        response = client.get("/celebration/mock-id")
        result = response.json()

        assert response.status_code == HTTPStatus.NOT_FOUND

        assert result["status_code"] == HTTPStatus.NOT_FOUND
        assert result["content"] is not None

        assert result["content"]["status_code"] is not None
        assert result["content"]["message"] is not None
