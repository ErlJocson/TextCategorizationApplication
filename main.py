from fastapi import FastAPI
from fastapi.responses import JSONResponse
import app.users.routes as user_router
import app.session.routes as session_router
import app.query.routes as query_router

app = FastAPI(
    title = 'Text Categorization Application',
    description = 'This is just a replication of some funcitonalities of Nexidia',
    version = '0.1.0'
)

app.include_router(user_router.router)
app.include_router(session_router.router)
app.include_router(query_router.router)



