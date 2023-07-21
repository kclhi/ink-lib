import logging, os, base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)

from ink.bard import Bard
from ink.ink_types import Chatbot, InkMessages


class Ink:
    def __init__(self) -> None:
        self.__logger: logging.Logger = logging.getLogger()

    def sendMessage(self, message: str) -> str:
        bard: Chatbot = Bard()
        return bard.sendMessage(message)

    def signMessages(self, messages: InkMessages) -> str:
        with open(os.environ['privateKeyPath'], 'rb') as pemFile:
            privateKey: bytes = pemFile.read()
        signedMessage: bytes = load_pem_private_key(privateKey, password=None).sign(
            ''.join(messages.messages).encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
        encodedSignedMessage: str = base64.b64encode(signedMessage).decode('utf-8')
        self.__logger.debug(encodedSignedMessage)
        return encodedSignedMessage

    def verifySignature(self, signedMessages: str, messages: InkMessages) -> bool:
        with open(os.environ['publicKeyPath'], 'rb') as pemFile:
            publicKey: bytes = pemFile.read()
        try:
            load_pem_public_key(publicKey).verify(
                base64.b64decode(signedMessages.encode('utf-8')),
                ''.join(messages.messages).encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
            return True
        except:
            return False
