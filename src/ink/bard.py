import os, logging
from bardapi import Bard as BardAPI  # type: ignore
from ink.ink_types import BardResponse


class Bard:
    def __init__(self) -> None:
        self.__logger: logging.Logger = logging.getLogger()
        self.__bard: BardAPI = BardAPI(token=os.environ['token'])

    def sendMessage(self, message: str) -> str:
        response: BardResponse = BardResponse(**self.__bard.get_answer(message))
        self.__logger.debug(response.content)
        return response.content
