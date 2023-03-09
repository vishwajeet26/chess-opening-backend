from fastapi import FastAPI
import app.models as models, app.database as database
from .routers import openings

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(openings.router)
