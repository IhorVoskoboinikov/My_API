# создание Endpoints для разных операций
from typing import List, Optional
from fastapi import APIRouter, Depends, Response, status


from ..models.operations import User, OperationStatus, CreateUser, UpdateUser
from ..services.operations import OperationService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[User])
def get_all_users(
        status: Optional[OperationStatus] = None,  # чтобы данный параметр был НЕ обязательным -> None
        service: OperationService = Depends()

):
    return service.get_list(status=status)


@router.post('/', response_model=User)
def create_user(
        user_data: CreateUser,
        service: OperationService = Depends(),

):
    return service.create(user_data)


@router.get('/{user_id}', response_model=User)
def get_user(
        user_id: int,
        service: OperationService = Depends()
):
    return service.get_user(user_id)


@router.put('/{user_id}', response_model=User)
def update_user(
        user_id: int,
        user_data: UpdateUser,
        service: OperationService = Depends()
):
    return service.update(user_id, user_data)


@router.delete('/{user_id}')
def delete_user(
        user_id: int,
        service: OperationService = Depends()
):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
