from dataclasses import dataclass
from typing import Protocol


@dataclass
class BardChoice:
    id: str
    content: list[str]


@dataclass
class ChatbotResponse:
    content: str
    conversation_id: str


@dataclass
class BardResponse(ChatbotResponse):
    content: str
    conversation_id: str
    response_id: str
    factualityQueries: str | None
    textQuery: list[str | int]
    choices: list[str]
    links: list[str]
    images: set[str]
    code: str | None
    langCode: str


@dataclass
class InkMessage:
    sender: str
    text: str
    conversationId: str | None = None


class Chatbot(Protocol):
    def sendMessage(self, message: str) -> ChatbotResponse:
        ''''''
