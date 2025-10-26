from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.users.models import User
from app.users.serializers import UserResponse

router = APIRouter(prefix = '/api/user')

@router.get('/get-one-user/{user_id}', response_model = UserResponse)
async def get_one_user(user_id: str) -> UserResponse:
    
    return JSONResponse(
        status_code = 200,
        content = {
            "mgs":"User was found."
        }
    )


@router.get('get-all-users/{limit}', response_model = list[UserResponse])
async def get_all_users(limit: int = 10) -> list[UserResponse]:
    return


@router.post('/create-user', response_model = UserResponse)
async def create_user() -> UserResponse:
    return


@router.delete('/delete-user/{user_id}', response_model = UserResponse)
async def delete_user(user_id: int) -> UserResponse:
    return


@router.put('/update-user/{user_id}', response_model = UserResponse)
async def update_user(user_id: int) -> UserResponse:
    return



