from fastapi import APIRouter
from src.api.ad.controller import ad_route

api = APIRouter()


api.include_router(router=ad_route, prefix="/ad")