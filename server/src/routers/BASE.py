'''
	This file contains third party libraries used accross all current
	routes files 
'''
from fastapi import APIRouter, FastAPI, status
from fastapi import Response, Depends, HTTPException
from fastapi.responses import JSONResponse