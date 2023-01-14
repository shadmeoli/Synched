from fastapi import APIRouter, FastAPI, status
from fastapi import Response, Depends, HTTPException
from fastapi.responses import JSONResponse


# router object
router = APIRouter(
    prefix="/synched/search-",
    tags=['account-access'],
    responses={ 404: {"description" : "Not Found"}}
    )

# user registration
@router.post('/sign-up')
async def user_signup(details):
    return details


# user registration
@router.post('/sign-in')
async def user_signin(details):
    return details


# deleting an account
@router.delete('/delete-account')
async def user_signin(details):
    return details
