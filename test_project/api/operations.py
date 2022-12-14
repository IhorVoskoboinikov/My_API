from typing import List, Optional
from fastapi import APIRouter, Depends, Response, status

from ..models.operations import User, OperationStatus, CreateUser
from ..services.operations import OperationService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[User])
def get_all_users(
        status: Optional[OperationStatus] = None,
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


@router.delete('/{user_id}')
def delete_user(
        user_id: int,
        service: OperationService = Depends()
):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{user_id}', response_model=User)
def enter_and_out_the_game(
        status: OperationStatus,
        user_id: int,
        service: OperationService = Depends()
):
    return service.enter_and_out_the_game(user_id, status)
