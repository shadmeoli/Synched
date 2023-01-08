from dataclasses import dataclass

from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from fastapi import Response, Depends

# all routes
from routers import playlist_action, search_music

# from Model.schema import UserRegistration



# server initilzation with configs
app = FastAPI(
    title="Synched",
    description="An app to help DJs find compatible songs by\n **BPM, GENRE, COUNTRY AND POPULARITY**",
    version="0.0.1",
    contact={
            "name": "Shadrack Meoli",
            "email": "shadcodes@gmail.com"
    },
    redoc_url="/redoc"
)


# pluging in the routes to the entry file
app.include_router(playlist_action.router)
app.include_router(search_music.router)