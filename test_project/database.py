from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .setings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}  # для работы в одно потоковом режиме
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)  # взаимодействие с базой данных, autocommit, autoflush делаем в ручную
# для единоразового создания базы создаем через python console,
# это как единоразовый вариант (сейчас реализация в файле app.py)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()

