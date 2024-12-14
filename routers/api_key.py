from fastapi import APIRouter, HTTPException, status, Depends
from auth.security import get_api_key

router=APIRouter()

@router.get('/')
def validate_key(api_key:str=Depends(get_api_key)):
    return{"message": "API KEY IS VALID"}

