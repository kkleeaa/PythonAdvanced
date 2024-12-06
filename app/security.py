from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_NAME="api-key"

api_key_header=APIKeyHeader(name=API_KEY_NAME, auto_error= False)

def get_api_key (api_key:str= Depends (api_key_header)):
    allowed_api_key=os.getenv("API_KEY", "").strip(",")
    print("Received API key:", api_key)
    print("Allowed API key:", allowed_api_key)
    if api_key not in api_key_header:
        print("API key is invalid")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid API key"

        )
    print ("API key is valid")
    return api_key
