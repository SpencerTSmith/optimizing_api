from contextlib import contextmanager
from typing import Generator

from gymhero.database.session import SessionLocal
from gymhero.log import get_logger

logger = get_logger(__name__)


def get_db() -> Generator:
    """
    Generate the database session.

    This function returns a generator object that provides a database session.
    The session is created using the `SessionLocal` class.

    Returns:
        Generator: A generator that yields the database session.

    Raises:
        Exception: If an error occurs while creating the session.

    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(
            "An error occurred while getting the database session. Error: %s", e
        )
        raise e
    finally:
        db.close()


@contextmanager
def get_ctx_db() -> Generator:
    """
    A context manager that provides a database session.

    This function returns a generator object that provides a database session.
    The session is created using the `SessionLocal` class.

    Returns:
        Generator: A generator that yields the database session.

    Raises:
        Exception: If an error occurs while creating the session.

    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(
            "An error occurred while getting the database session. Error: %s", e
        )
        raise e
    finally:
        db.close()
