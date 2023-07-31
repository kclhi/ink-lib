import os, logging, requests
from bardapi import Bard as BardAPI  # type: ignore
import requests
from ink.ink_types import BardResponse


class Bard:
    def __init__(self, session: requests.Session | None = None) -> None:
        self.__logger: logging.Logger = logging.getLogger()
        self.__bard: BardAPI = BardAPI(token=os.environ['token'], session=session)

    def sendMessage(self, message: str) -> BardResponse:
        response: BardResponse = BardResponse(**self.__bard.get_answer(message))
        self.__logger.debug(response.content)
        return response
