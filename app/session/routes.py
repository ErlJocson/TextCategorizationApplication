from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.session.models import Session
from app.session.serializers import SessionResponse, SessionUpdate, SessionCreate
from app.database import db_dependency
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix = '/api/session')

@router.get('/get-one-sesion/{session_id}', response_model = SessionResponse)
def get_one_session(session_id: str, db: db_dependency) -> SessionResponse:
    session = db.query(Session).filter_by(session_id = session_id).firsts()
    if session is None:
        raise HTTPException(
            status_code = 404,
            detail = f'{session} does not exist'
        )
    return session


@router.get('/get-all-sessions', response_model = SessionResponse)
def get_all_sessions(db: db_dependency) -> SessionResponse:
    sessions = db.query(Session).all()

    if sessions is None:
        raise HTTPException(
            status_code = 404,
            detail = 'There are no sessions'
        )
    return sessions


@router.post('/create-session', response_model = SessionResponse)
def create_session(session: SessionCreate, db: db_dependency) -> SessionResponse:
    db_session = Session(**session.dict())

    try:
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        return db_session

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code = 404, detail = f'User already exist in the database')

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code = 404, detail = f'Unexpected error occured: {str(e)}')


@router.put('/update-session/{session_id}', response_model = SessionResponse)
def update_session(session_id: str, session_update: SessionUpdate, db: db_dependency) -> SessionResponse:
    session_to_update = db.query(Session).filter_by(session_id = session_id).first()

    if session_to_update is None:
        return HTTPException(status_code = 404, detail = f'{session} session does not exist')

    for key, value in session_update.dict(exclude_unset = True).items():
        setattr(session_to_update, key, value)

    db.commit()
    db.refresh()

    return session_to_update


@router.delete('/delete-session/{session_id}', response_model = SessionResponse)
def delete_session(session_id: str, db: db_dependency) -> SessionResponse:
    sesssion_to_delete = db.query(Session).filter_by(session_id = session_id).first()

    if session_to_delete is None:
        raise HTTPException(status_code = 404, detail = f'{session_id} session does not exist')

    db.delete(session_to_delete)
    db.commit()

    return session_to_delete


