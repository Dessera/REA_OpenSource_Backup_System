from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
import uvicorn

from config import user
import rea_db


def create_app():
    rea_db.init()
    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"Hello": "World"}

    return app


uvicorn.run(create_app(), host=user.host, port=user.port)
