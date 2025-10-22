from fastapi import APIRouter, HTTPException
from app.users.models import Users

router = APIRouter(prefix = '/api/user')


@router.get('/get-one-user/{user_id}', response_model = Users)
async def get_one_user(user_id: int) -> Users:
    return


@router.get('get-all-users', response_model = list[Users])
async def get_all_users() -> list[Users]:
    return


@router.post('/create-user')
async def create_user():
    return


@router.delete('/delete-user/{user_id}')
async def delete_user(user_id: int):
    return


@router.put('/update-user/{user_id}')
async def update_user(user_id: int):
    return



