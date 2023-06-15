from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.routers.drinks import Drink
from pydantic import BaseModel
import json

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

class OrderItem(BaseModel):
    """
    Represents an item in an order containing a drink and its quantity.

    Attributes:
        drink (Drink): The drink object.
        quantity (int): The quantity of the drink.
    """
    drink: Drink
    quantity: int


@router.post("")
def create_order(order: list[OrderItem]):
    """
    Create an order with the specified drink items and their quantities.

    Args:
        order (list[OrderItem]): The list of order items.

    Returns:
        dict: A success message indicating the order has been created.
    """
    print(order)
    return {"message": "Order created successfully"}
