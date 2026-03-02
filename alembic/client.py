"""Vertex AI client for Terpedia."""

from __future__ import annotations

from vertexai.generative_models import GenerativeModel

from alembic.config import get_location, get_model_id, get_project_id


class VertexClient:
    """Thin wrapper around Vertex AI Generative Model for Terpedia."""

    def __init__(
        self,
        *,
        project_id: str | None = None,
        location: str | None = None,
        model_id: str | None = None,
    ) -> None:
        self._project_id = project_id or get_project_id()
        self._location = location or get_location()
        self._model_id = model_id or get_model_id()
        self._model: GenerativeModel | None = None

    def _get_model(self) -> GenerativeModel:
        if self._model is None:
            import vertexai
            vertexai.init(project=self._project_id, location=self._location)
            self._model = GenerativeModel(self._model_id)
        return self._model

    def generate(
        self,
        prompt: str,
        *,
        system_instruction: str | None = None,
        max_output_tokens: int = 2048,
    ) -> str:
        """Generate a single response from the model."""
        model = self._get_model()
        kwargs = {"max_output_tokens": max_output_tokens}
        if system_instruction:
            kwargs["system_instruction"] = system_instruction
        response = model.generate_content(prompt, **kwargs)
        if not response.candidates or not response.candidates[0].content.parts:
            return response.text or ""
        return response.candidates[0].content.parts[0].text

    def chat(self, system_instruction: str | None = None) -> "ChatSession":
        """Start a multi-turn chat session."""
        return ChatSession(client=self, system_instruction=system_instruction)


class ChatSession:
    """Multi-turn chat with history."""

    def __init__(
        self,
        client: VertexClient,
        system_instruction: str | None = None,
    ) -> None:
        self._client = client
        model = client._get_model()
        self._chat = model.start_chat(
            system_instruction=system_instruction or ""
        )

    def send(self, message: str) -> str:
        response = self._chat.send_message(message)
        text = getattr(response, "text", None)
        if text is not None:
            return text
        if response.candidates and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        return ""
