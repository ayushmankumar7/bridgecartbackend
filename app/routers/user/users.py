from fastapi import APIRouter
# from schemas.user import User
from api.v1.endpoints.data import get_item_by_id, get_item_ids

router = APIRouter()

# @router.post('/')
# def create_user(user: User):
#     try:
#         uid = str(user.id)
#         doc_ref = db.collection(config.USER_TABLE_STR).document(uid)
#         user_ref = doc_ref.get()

#         if user_ref.exists:
#             return {'status': 'error', 'message': 'User already exists'}

#         doc_ref.set(user.to_json())
#         return {'status': 'success', 'data': user}
#     except:
#         return {'status': 'error', 'message': 'An exception occurred'}


# @router.get('/')
# def read_users(limit: str = 10):
#     try:
#         users_ref = db.collection(config.USER_TABLE_STR).limit(limit)
#         data = users_ref.stream()

#         return {'status': 'success', 'data': data}
#     except:
#         return {'status': 'error', 'message': 'An exception occurred'}


@router.get("/{instagram_username}/items/{item_id}")
def read_item(instagram_username:str, item_id: int):
    print("sample output")
    dic = get_item_by_id(instagram_username, item_id)
    print(dic)
    if(dic==None):
        dic={}
    dic["id"] = 1 
    dic["name"] = "Zip Tote Basket"
    dic["color"] = "White and black"
    dic["price"] = "Rs 1400"
    
    return [dic]

@router.get("/{instagram_username}/items/get_products/")
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

@router.get("/{instagram_username}/items/product_ids/")
def read_items(instagram_username: str):
    return get_item_ids(instagram_username)