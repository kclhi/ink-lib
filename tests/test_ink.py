import base64
from ink.ink_types import InkMessage
import pytest  # type: ignore
from dotenv import load_dotenv
from ink.ink import Ink


@pytest.fixture(scope='session', autouse=True)
def load_env() -> None:
    load_dotenv()


def test_Ink() -> None:
    ink: Ink = Ink()
    message: str = ink.sendMessage('hello world')
    assert type(message) == str and len(message) > 0
    signedMessages: str = ink.signMessages([InkMessage(sender='bob', text=message)])
    assert len(signedMessages) > 0
    assert ink.verifySignature(signedMessages, [InkMessage(sender='bob', text=message)])
    assert not ink.verifySignature(
        base64.b64encode(bytes('foo', 'utf-8')).decode('utf-8'),
        [InkMessage(sender='bob', text=message)],
    )
