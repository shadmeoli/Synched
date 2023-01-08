from fastapi import APIRouter, FastAPI, status
from fastapi import Response, Depends, HTTPException
from fastapi.responses import JSONResponse


# router object
router = APIRouter(
    prefix="/synched/playlist-actions",
    tags=['account-access'],
    responses={ 404: {"description" : "Not Found"}}
    )

# user registration
@router.post('/my-playlist')
async def my_playlist(details):
    return details


# user registration
@router.post('/saved-playlist')
async def saved_playlist(details):
    return details


# deleting an account
@router.delete('/recommendations')
async def playlist_recommendation(details):
    return details
