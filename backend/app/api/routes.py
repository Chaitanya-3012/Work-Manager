from fastapi import APIRouter # type: ignore

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Item Name"}