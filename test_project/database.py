from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .setings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}  # to work in single-threaded mode
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
