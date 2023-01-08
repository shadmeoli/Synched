from fastapi import APIRouter, FastAPI, status
from fastapi import Response, Depends, HTTPException
from fastapi.responses import JSONResponse


# router object
router = APIRouter(
    prefix="/synched/search-action",
    tags=['account-access'],
    responses={ 404: {"description" : "Not Found"}}
    )

# user registration
@router.post('/search-result')
async def playlist_from_search(details):
    return details

# user registration
@router.post('/search-result')
async def recommendation_from_search(details):
    return details


# user registration
@router.post('/BPM-result')
async def filter_by_BPM(details):
    return details

# user registration
@router.post('/genre-result')
async def filter_by_genre(details):
    return details

# user registration
@router.post('/country-result')
async def filter_by_country(details):
    return details

# user registration
@router.post('/popularity-result')
async def filter_by_popularity(details):
    return details