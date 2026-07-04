from unittest.mock import patch

from app.food_detector import detect_food


class _FakeMessage:
    def __init__(self, content):
        self.content = content


class _FakeChoice:
    def __init__(self, content):
        self.message = _FakeMessage(content)


class _FakeResponse:
    def __init__(self, content):
        self.choices = [_FakeChoice(content)]


def test_detect_food_uses_supported_model_slug():
    with patch(
        "app.food_detector.client.chat.completions.create",
        return_value=_FakeResponse("pizza"),
    ) as mock_create:
        result = detect_food(b"fake-image-bytes")

        assert result == "pizza"
        assert (
            mock_create.call_args.kwargs["model"]
            == "google/gemma-3-27b-it"
        )