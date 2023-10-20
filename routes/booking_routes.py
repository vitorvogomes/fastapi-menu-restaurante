from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from models.booking_models import BookingModel, BookingStatusModel
from utils.booking_querys import *

booking_router = APIRouter()

@booking_router.get("/booking", status_code=status.HTTP_200_OK)
async def booking_list(date: str | None = None, status: str | None = None):
    try:
        if date or status:
            booking_list = booking_query_params(date, status)
            return {"reservas": formatted_list(booking_list)}
        else:
            booking_list = get_booking_list()
            return {"reservas": formatted_list(booking_list)}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )

@booking_router.post("/booking", status_code=status.HTTP_201_CREATED)
async def create_new_booking(booking_data: BookingModel):
    try:
        booking = validate_client_booking(booking_data.booking_date, booking_data.client_email)
        if not booking:
            booking_list = get_booking_list()
            crowd = count_total_people(booking_list)
            if crowd:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": f"O número máximo de pessoas para reservas no restaurante já foi ultrapassado."}
                )
            else:
                create_booking(
                    booking_data.num_people,
                    booking_data.booking_status,
                    booking_data.booking_date,
                    booking_data.client_email
                )
                return {"success": f"A reserva do cliente: '{booking_data.client_email}', foi marcada para o dia '{booking_data.booking_date}'. "}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Já existe uma reserva para o cliente: '{booking_data.client_email}', no dia '{booking_data.booking_date}'."
        )

@booking_router.patch("/booking/{booking_id}", status_code=status.HTTP_200_OK)
async def update_booking_status(booking_id: str, new_status: BookingStatusModel):
    try:
        booking = get_booking_by_id(booking_id)
        if booking:
            update_booking(booking_id, new_status.value)
            return {"success": f"A o status da reserva foi alterado para: '{new_status.value}'."}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_UNAUTHORIZED,
            detail=f"A reserva com o id: '{booking_id}' não foi localizada."
        )

def formatted_list(data):
    booking_data = []
    for item in data:
        item_data = {
            "booking_id": item[0],
            "num_people": item[1],
            "booking_status": item[2],
            "booking_date": item[3],
            "client_email": item[4]
        }
        booking_data.append(item_data)
    return booking_data

def count_total_people(data):
    total_people = 0
    for item in data:
        total_people += item[1]
    
    if total_people > 150:
        return True
    else:
        return False
