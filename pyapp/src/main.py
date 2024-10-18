from dotenv import load_dotenv
from fastapi import FastAPI

from src.infra.containers import Container
from src.infra.routers.v1.balances import router as balances_router


def create_app() -> FastAPI:
    load_dotenv()
    app = FastAPI(docs_url="/docs")
    
    container = Container()
    app.container = container
    
    database = container.database()
    database.create_database()
    
    app.include_router(router=balances_router)
    
    return app


app = create_app()
