from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.session.models import Session
from app.session.serializers import SessionResponse

router = APIRouter(prefix = '/api/session')

@router.get('/get-one-sesion/{session_id}', response_model = SessionResponse)
def get_one_session(session_id: int) -> SessionResponse:
    return 

@router.get('/get-all-sessions', response_model = SessionResponse)
def get_all_sessions() -> SessionResponse:
    return JSONResponse(
        content = {"data":[]},
        status_code = 200
    )

@router.post('/create-session', response_model = SessionResponse)
def create_session() -> SessionResponse:
    return

@router.put('/update-session/{session_id}', response_model = SessionResponse)
def update_session(session_id: int) -> SessionResponse:
    return


@router.delete('/delete-session/{session_id}', response_model = SessionResponse)
def delete_session(session_id: int) -> SessionResponse:
    return
