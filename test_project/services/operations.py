from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from test_project.database import get_session
from .. import tables
from ..models.operations import OperationStatus, CreateUser, UpdateUser


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.Operation:
        operation = (
            self.session
            .query(tables.Operation)
            .filter_by(id=user_id)
            .first()
        )
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get_list(self, status: Optional[OperationStatus] = None) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if status:
            query = query.filter_by(status=status)
        operations = (query.all())
        return operations

    def get_user(self, user_id: int) -> tables.Operation:
        return self._get(user_id)

    def create(self, user_data: CreateUser) -> tables.Operation:
        operation = tables.Operation(**user_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, user_id: int, user_data: UpdateUser) -> tables.Operation:
        operation = self._get(user_id)
        for field, value in user_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, user_id: int):
        operation = self._get(user_id)
        self.session.delete(operation)
        self.session.commit()
