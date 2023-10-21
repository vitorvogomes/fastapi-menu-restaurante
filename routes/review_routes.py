from fastapi import HTTPException, APIRouter, status

from models.review_models import ReviewModel
from utils.review_querys import *

from datetime import datetime

review_router = APIRouter()

@review_router.get("/reviews", status_code=status.HTTP_200_OK)
def review_list(score: int | None = None, date: str | None = None):
    try:
        if score or date:
            review_list = review_query_params(score, date)
        else:
            review_list = get_review_list()
        return {"reviews": formatted_list(review_list)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )

@review_router.post("/reviews", status_code=status.HTTP_201_CREATED)
def create_new_review(review_data: ReviewModel):
    try:
        create_review(
            review_data.review_description,
            review_data.review_score,
            review_data.client_email
        )
        return {"success": "Sua avaliação foi postada!"}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )

def formatted_list(data):
    review_data = []
    for item in data:
        item_data = {
            "review_id": item[0],
            "review_description": item[1],
            "review_score": item[2],
            "review_date": item[3],
            "client_email": item[4]
        }
        review_data.append(item_data)
    
    return review_data

