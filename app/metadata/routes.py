from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.metadata.models import MetaInfo
from app.metadata.serializers import MetaInfoBase, MetaInfoCreate, MetaInfoUpdate, MetaInfoResponse
from app.database import db_dependency
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix = '/api/metadata')

@router.get('/get-one-metainfo/{metainfo_id}', response_model = MetaInfoResponse)
async def get_one_metainfo(metainfo_id : str, db: db_dependency) -> MetaInfoResponse:
    metainfo = db.query(MetaInfo).filter_by(metainfo_id = metainfo_id).first()

    if metainfo is None:
        raise HTTPException(status = 404, detail = f"{metainfo_id} does not exist")

    return metainfo


@router.get('/get-all-metainfo', response_model = MetaInfoResponse)
async def get_all_metainfo(metainfo_id: str, db: db_dependency) -> MetaInfoResponse:
    all_metainfo = db.query(MetaInfo).all()
    if all_metainfo is None:
        raise HTTPException(status = 404, detail = f'No metainfo exist')

    return all_metainfo

@router.post('/create-metainfo', response_model = MetaInfoResponse)
async def create_metainfo(metainfo: MetaInfoCreate, db: db_dependency) -> MetaInfoResponse:
    db_metainfo = MetaInfo(**metainfo.dict())

    try:
        db.add(metainfo)
        db.commit()
        db.refresh
        return db_metainfo

    except IntegrityError:
        db.rollback()
        raise HTTPException(status = 404, detail = f'Metainfo already exist')

    except Exception as e:
        db.rollback()
        raise HTTPException(status = 404, detail = f'Unexpected error: {e}')


@router.delete('/delete-metainfo/{metainfo_id}', response_model = MetaInfoResponse)
async def delete_metadata(metainfo_id: str, db: db_dependency) -> MetaInfoResponse:
    metainfo_to_delete = db.query(MetaInfo).filter_by(metainfo_id = metainfo_id).first()
    if metainfo_to_delete is None:
        raise HTTPException(status = 404, detail = f"{metainfo_id} does not exist")

    db.delete(metainfo_to_delete)
    db.commit()

    return metainfo_to_delete


@router.put('/update-metainfo/{metainfo_id}', response_model = MetaInfoResponse)
def update_metadata(metainfo_id: str, db: db_dependency):
    metainfo_to_update = db.query(MetaInfo).filter_by(metainfo_id = metainfo_id).first()

    if metainfo_to_update is None:
        raise HTTPException(status = 404, detail = f'{metainfo_id} does not exist')


    for key, value in metainfo_to_update.dict(exclude_unset = True).items():
        setattr(metainfo_to_update, key, value)


    db.commit()
    db.refresh()

    return metainfo_to_update
