from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix = '/api/session')

@router.get('/get-one-sesion/{session_id}')
def get_one_session(session_id: int):
    return 

@router.get('/get-all-sessions')
def get_all_sessions():
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



