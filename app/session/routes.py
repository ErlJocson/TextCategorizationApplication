from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.session.models import SessionManagement

router = APIRouter(prefix = '/api/session')

@router.get('/get-one-sesion/{session_id}', response_model = SessionManagement)
def get_one_session(session_id: int) -> SessionManagement:
    return 

@router.get('/get-all-sessions', response_model = list[SessionManagement])
def get_all_sessions() -> list[SessionManagement]:
    return JSONResponse(
        content = {"data":[]},
        status_code = 200
    )

@router.post('/create-session')
def create_session():
    return

@router.put('/update-session/{session_id}')
def update_session(session_id: int):
    return


@router.delete('/delete-session/{session_id}')
def delete_session(session_id: int):
    return



