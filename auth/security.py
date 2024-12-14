from fastapi import FastApi, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

from app.security import API_KEY_NAME, api_key_header

load_dotenv()
API_KEY=os.getenv("API_KEY")
API_KEY_NAME="api-key"
api_key_header=APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str=Depends(api_key_header)):
    if api_key!=API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api key"
        )
    return api_key 