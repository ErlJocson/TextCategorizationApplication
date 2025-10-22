from fastapi import FastAPI
from fastapi.responses import JSONResponse
import app.users.routes as user_router
import app.session.routes as session_router

app = FastAPI(title = 'Text Categorization Application')

app.include_router(user_router.router)
app.include_router(session_router.router)

@app.get("/")
def root_route():
    return JSONResponse(
        content = {
            "title":"Text Categorization Application",
            "message":"This is just a side project which replicates some of the features of nexidia. features included are Session Building, Query Building, and User Creation. In the future, sentiment scoring will also be added - the basis ones that is also available in python",
            "author":"Erl Jocson",
            },
        status_code = 200
    )


