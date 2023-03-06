from fastapi import FastAPI
import app.models as models, app.database as database
# import sys
# sys.path.insert(1, 'routers') 
# import openings
# import routers.openings
from .routers import openings

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(openings.router)
