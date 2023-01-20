from .BASE import *

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
@router.get('/search-result')
async def recommendation_from_search(details):
    return details

# user registration
@router.get('/BPM-result')
async def filter_by_BPM(details):
    return details

# user registration
@router.get('/genre-result')
async def filter_by_genre(details):
    return details

# user registration
@router.get('/country-result')
async def filter_by_country(details):
    return details

# user registration
@router.get('/popularity-result')
async def filter_by_popularity(details):
    return details