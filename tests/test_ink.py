import base64
from zoneinfo import ZoneInfo
import pytest  # type: ignore
from datetime import datetime
from dotenv import load_dotenv

from ink.ink import Ink
from ink.ink_types import InkMessage


@pytest.fixture(scope='session', autouse=True)
def load_env() -> None:
    load_dotenv()


def test_sendMessage() -> None:
    ink: Ink = Ink()
    message: str = ink.sendMessage('hello world')
    assert type(message) == str and len(message) > 0


def test_signMessage() -> None:
    ink: Ink = Ink()
    signedMessages: str = ink.signMessages(
        [InkMessage(sender='bob', text='hello world')]
    )
    assert len(signedMessages) > 0


def test_verifySignature() -> None:
    ink: Ink = Ink()
    signedMessages: str = ink.signMessages(
        [InkMessage(sender='bob', text='hello world')]
    )
    assert len(signedMessages) > 0
    assert ink.verifySignature(
        signedMessages, [InkMessage(sender='bob', text='hello world')]
    )
    assert not ink.verifySignature(
        base64.b64encode(bytes('foo', 'utf-8')).decode('utf-8'),
        [InkMessage(sender='bob', text='hello world')],
    )


def test_getTimestamp() -> None:
    ink: Ink = Ink()
    signedMessages: str = ink.signMessages(
        [InkMessage(sender='bob', text='hello world')]
    )
    assert len(signedMessages) > 0
    assert len(ink.getTimestamp(signedMessages)) > 0


def test_verifyTimestamp() -> None:
    ink: Ink = Ink()
    signedMessages: str = ink.signMessages(
        [InkMessage(sender='bob', text='hello world')]
    )
    assert len(signedMessages) > 0
    timestamp: str = ink.getTimestamp(signedMessages)
    assert len(timestamp) > 0
    assert ink.verifyTimestamp(signedMessages, timestamp)
    assert not ink.verifyTimestamp(
        base64.b64encode(bytes('foo', 'utf-8')).decode('utf-8'), timestamp
    )


def test_extractTime() -> None:
    ink: Ink = Ink()
    signedMessages: str = ink.signMessages(
        [InkMessage(sender='bob', text='hello world')]
    )
    assert len(signedMessages) > 0
    timeNow: datetime = datetime.now(tz=ZoneInfo('UTC'))
    timestamp: str = ink.getTimestamp(signedMessages)
    assert len(timestamp) > 0
    timestampTime: datetime = ink.extractTime(timestamp)
    assert timestampTime.hour == timeNow.hour and timestampTime.minute == timeNow.minute
