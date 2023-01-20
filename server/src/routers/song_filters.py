from .BASE import *

# router object
router = APIRouter(
    prefix="/synched/song_filters",
    tags=['account-access'],
    responses={ 404: {"description" : "Not Found"}}
)

# filtering song by genre
@router.get('/')
async def user_signup(details):
    return details