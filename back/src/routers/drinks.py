from fastapi import APIRouter
from pydantic import BaseModel

class Drink(BaseModel):
    '''
    Represents a drink.

    Attributes:
        name (str): The name of the drink.
        category (str): The category of the drink.
    '''
    name: str
    category: str

router = APIRouter(
    prefix="/drinks",
    tags=["drinks"]
)

@router.get("", response_model=list[Drink])
def get_drinks():
    '''
    Get drinks
    
    Retrieve the list of available drinks. 
    Returns:
        List[Drink]: The list of available drinks.
    '''
    drinks = [
        Drink(name="Cocktail 1", category="Category 1"),
        Drink(name="Cocktail 2", category="Category 2"),
        Drink(name="Cocktail 3", category="Category 1"),
    ]
    return drinks