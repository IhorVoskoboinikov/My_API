import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):

    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    email = sa.Column(sa.String)
    status = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)