from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.query.serializers import QueryResponse

router = APIRouter(prefix = '/api/query')


@router.get('/get-one-query/{query_id}', response_model = QueryResponse)
async def get_one_query(query_id: str) -> QueryResponse:
    return


@router.get('/get-all-query', response_model = list[QueryResponse])
async def get_all_query() -> list[QueryResponse]:
    return


@router.post('/create-query',  response_model = QueryResponse)
async def create_query() -> QueryResponse:
    return


@router.put('/update-query/{query_id}', response_model = QueryResponse)
async def update_query(query_id: str) -> QueryResponse:
    return


@router.delete('/delete-query/{query_id}', response_model = QueryResponse)
async def delete_query(query_id: str) -> QueryResponse:
    return

