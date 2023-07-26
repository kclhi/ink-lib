from dataclasses import dataclass
from typing import Protocol


@dataclass
class BardChoice:
    id: str
    content: list[str]


@dataclass
class BardResponse:
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


class Chatbot(Protocol):
    def sendMessage(self, message: str) -> str:
        ''''''
