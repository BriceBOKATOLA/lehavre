from fastapi import APIRouter, FastAPI
from routes import evenements
import database
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:3000"],  # Autorise cette origine spécifique
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)

database.Base.metadata.create_all(bind=database.engine)

# Inclut les routes
app.include_router(evenements.router)

