from email.quoprimime import body_check
from urllib import response
import pytest 
import requests
import json


def test_valid_login():
    url= "https://reqres.in/api/login/"
    data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    response = requests.post(url,data=data)
    token = json.loads(response.text)
    assert response.status_code==200
    assert token['token']=="QpwL5tke4Pnpja7X4"


def test_invalid_login():
    url= "https://reqres.in/api/login/"
    data = {"email": "abc@gmail.com","password": "adfsdf"}
    response = requests.post(url,data=data)
    token = json.loads(response.text)
    assert response.status_code==400
    

def test_list_users():
    url= "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    body = json.loads(response.text)
    assert response.status_code==200
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content
    # f = open("list_User.txt", "a")
    # f.write(str(body))
    # f.close()
    with open("list_User.txt", "w") as f:
        f.write(str(body))
    

def test_getSingle_user():
    url= "https://reqres.in/api/users/2"
    response = requests.get(url)
    assert response.status_code==200 or 201  

def test_getSingle_userNotFound():
    url= "https://reqres.in/api/users/23"
    response = requests.get(url)
    assert response.status_code==404 


def test_list_resource():
    url= "https://reqres.in/api/unknown"
    response = requests.get(url)
    assert response.status_code==200

@pytest.mark.PCreate
def test_post_create():
    url= "https://reqres.in/api/users"
    data = {"name": "peter","job": "leader"}
    response = requests.post(url,data=data)
    body=json.loads(response.text)
    assert response.status_code==201
    with open("post_create.txt","w") as f:
        f.write(str(body))


@pytest.mark.PutUpdate
def test_put_update():
    url= "https://reqres.in/api/users/2"
    data = {"name": "peter","job": "QA"}
    response = requests.put(url,data=data)
    body=json.loads(response.text)
    assert response.status_code==200
    with open("put_update.txt","w") as f:
        f.write(str(body))