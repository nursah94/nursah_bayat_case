import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/pet"
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def test_post_pet_success():
    payload = {
        "id": 5,
        "category": {"name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 3, "name": "string"}],
        "status": "available"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5

def test_post_pet_invalid_json():
    payload = {
        "id": 1,
        "category": {"name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": {
            "id": 3,
            "name": "string"
        },
        "status": "available"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 500 
    data = response.json()
    assert data["message"] == "something bad happened" 

def test_get_pet_success():
    response = requests.get(f"{BASE_URL}/5", headers={"accept": "application/json"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5

def test_get_pet_not_found():
    response = requests.get(f"{BASE_URL}/5466", headers={"accept": "application/json"})
    assert response.status_code == 404
    data = response.json()
    assert data["message"] == "Pet not found"

def test_put_pet_success():
    payload = {
        "id": 5,
        "category": {"id": 0, "name": "string"},
        "name": "updated-name",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }
    response = requests.put(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "updated-name"

def test_put_pet_invalid_json():
    payload = {
        "id": 0,
        "category": {"id": 0, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": {
            "id": 0,
            "name": "string"
        }, 
        "status": "available"
    }
    response = requests.put(BASE_URL, headers=HEADERS, json=payload)
    assert response.status_code == 500
    data = response.json()
    assert data["message"] == "something bad happened" 

def test_delete_pet_success():
    response = requests.delete(
        f"{BASE_URL}/5",
        headers={
            "accept": "application/json",
            "api_key": "special-key"
        }
    )
    assert response.status_code == 200  
    data = response.json()
    assert data["message"] == "5"  
    

def test_delete_pet_not_found():
    response = requests.delete(
        f"{BASE_URL}/5466",
        headers={
            "accept": "application/json",
            "api_key": "special-key"
        }
    )
    assert response.status_code == 404
