from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.users.models import User
from app.users.serializers import UserResponse, UserCreate, UserUpdate
from app.database import db_dependency
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix = '/api/user')

@router.get('/get-one-user/{user_id}', response_model = UserResponse)
async def get_one_user(user_id: str) -> UserResponse:
    user = db.query(User).filter_by(user_id = user_id).first()
    if user is None:
        raise HTTPExeption(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f'{user_id} does not exist'
        )    
    return user

@router.get('/get-all-users', response_model = list[UserResponse])
async def get_all_users(db: db_dependency) -> list[UserResponse]:
    users = db.query(User).all()
    if users is None:
        raise HTTPException(
            status_code = 404,
            detail = 'No user exists.'
        )
    return users


@router.post('/create-user', response_model = UserResponse)
async def create_user(user: UserCreate, db: db_dependency) -> UserResponse:
    db_user = User(**user.dict())
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists in the database."
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred: {str(e)}"
        )

@router.delete('/delete-user/{user_id}', response_model = UserResponse)
async def delete_user(user_id: str, db: db_dependency) -> UserResponse:
    user_to_delete = db.query(User).filter_by(user_id=user_id).first()

    if user_to_delete is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            details=f"{user_id} does not exist"
        )

    db.delete(user_to_delete)
    db.commit()

    return user_to_delete




@router.put('/update-user/{user_id}', response_model = UserResponse)
async def update_user(user_id: str, user_update: UserUpdate, db: db_dependency) -> UserResponse:
    user_to_update = db.query(User).filter_by(user_id = user_id).first()

    if user_to_update is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{user_id} not found")

    for key, value in user_update.dict(exclude_unset = True).items():
        setattr(user_to_update, key, value)

    db.commit()
    db.refresh()

    return user

