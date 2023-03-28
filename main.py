from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from database_stuffs.try1 import get_item_by_id, get_item_ids, get_items

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://192.168.0.113:3000",
    "http://192.168.0.104:3000",
    "http://192.168.0.113:8000",
    "http://192.168.0.104:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{instagram_username}/items/{item_id}")
def read_item(instagram_username:str, item_id: int):
    print("sample output")
    dic = get_item_by_id(instagram_username, item_id)
    print(dic)
    dic["id"] = 1 
    dic["name"] = "Zip Tote Basket"
    dic["color"] = "White and black"
    dic["price"] = "Rs 1400"
    
    return [dic]

@app.get("/{instagram_username}/items/get_products/")
def get_page(instagram_username: str):
    items = []
    ids = get_item_ids(instagram_username)
    print(ids)
    for id in ids[1:]:
        item = get_item_by_id(instagram_username, id)
        item["id"] = 1 
        item["name"] = "Zip Tote Basket"
        item["color"] = "White and black"
        item["price"] = "Rs 1400"
        items.append(item)
    return items

@app.get("/{instagram_username}/items/product_ids/")
def read_items(instagram_username: str):
    return get_item_ids(instagram_username)