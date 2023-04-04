from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app
from core.config import config
client = TestClient(app=app)

base_url = config.API_V1_STR
# product tests
def test_create_product():
    response = client.post(f"{base_url}/product/",
                           json={
        "id":1234,
        "title":"Mango book",
        "caption":"blablabla",
        "description":"blabla",
        "image":[],
        "price":45.0,
        "category":"cookies",
        "variant":"blue",
        "username":"governedbyprudence"
    })
    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {"message":"succesfully created"}

def test_get_products_by_username():
    username = "governedbyprudence"
    productId = "1234567"
    response = client.get(f"{base_url}/{username}/product/{productId}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'id': 1234567, 'title': 'Django book', 'caption': 'blablabla', 'description': 'blabla', 'image': [], 'price': 45.0, 'created_at': '2023-04-05T03:04:45.924773+00:00', 'category': 'book', 'variant': 'blue'}


def test_get_products_by_category():
    username = "governedbyprudence"
    category = "book"
    response = client.get(f"{base_url}/{username}/product-by-category/{category}")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'id': 123456, 'title': 'Django book', 'caption': 'blablabla', 'description': 'blabla', 'image': [], 'price': 45.0, 'created_at': '2023-04-05T02:53:08.845396+00:00', 'category': 'book', 'variant': 'blue'}, {'id': 1234567, 'title': 'Django book', 'caption': 'blablabla', 'description': 'blabla', 'image': [], 'price': 45.0, 'created_at': '2023-04-05T03:04:45.924773+00:00', 'category': 'book', 'variant': 'blue'}]

# user tests

def test_create_user():
    data = {
        "id":"governedbyprudence",
        "email":"punnyarthabanerjee@gmail.com",
        "password":"admin345",
        "name":"Punnyartha Banerjee",
    }
    response = client.post(f"{base_url}/signup",json=data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message":"Registration successful"} 

def test_login_user():
    response = client.post(f"{base_url}/login",json={
        "email":"punnyarthabanerjee@gmail.com",
        "password":"admin345"
    })
    
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.json() 
    '''
    reponse will be something like this
    {'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImdvdmVybmVkYnlwcnVkZW5jZSIsImZpcmViYXNlX2lkIjpudWxsLCJlbWFpbCI6InB1bm55YXJ0aGFiYW5lcmplZUBnbWFpbC5jb20iLCJwYXNzd29yZCI6IiRwYmtkZjItc2hhMjU2JDI5MDAwJHNkWTZCLkM4dDVZU0lnUWdCT0RjV3ckb3FhbGxpbmRQUmlJL2ZoaWVBSjhJcUZIdzRBUnkxTHBLSk1KbkE3V0E2cyIsIm5hbWUiOiJQdW5ueWFydGhhIEJhbmVyamVlIiwibm90ZSI6bnVsbCwiYWN0aXZlIjp0cnVlfQ.LYbgVf5tBzSL178Pk_fIl-bVm-C_1GPuIK-9lGDldsA'}
    '''

if __name__ == "__main__":
    pytest.main()

