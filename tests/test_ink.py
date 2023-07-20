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
