from fastapi import APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer

router = APIRouter(tags=["auth"])
