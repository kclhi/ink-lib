import logging
from ink.bard import Bard
from ink.ink_types import Chatbot


class Ink:
    def __init__(self) -> None:
        self.__logger: logging.Logger = logging.getLogger()

    def sendMessage(self, message: str) -> str:
        bard: Chatbot = Bard()
        return bard.sendMessage(message)
