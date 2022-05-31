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

@pytest.mark.PatchUpdate
def test_patch_update():
    url= "https://reqres.in/api/users/2"
    data = {"name": "peter","job": "QA Enginer"}
    response = requests.patch(url,data=data)
    body=json.loads(response.text)
    assert response.status_code==200
    with open("patch_update.txt","w") as f:
        f.write(str(body))

def test_delete_user():
    url= "https://reqres.in/api/2"
    response = requests.delete(url)
    assert response.status_code==204

def test_register_user():
    url= "https://reqres.in/api/register"
    data = {"email": "eve.holt@reqres.in","password": "pistol"}
    response = requests.post(url,data=data)
    token = json.loads(response.text)
    assert response.status_code==200
    assert token['token']=="QpwL5tke4Pnpja7X4"

def test_register_unsuccessful():
    url= "https://reqres.in/api/register"
    data = {"email": "eve.holt@reqres.in"}
    response = requests.post(url,data=data)
    assert response.status_code==400

@pytest.mark.deleyed   
def test_deleyed_response():
    url= "https://reqres.in/api/users?delay=3"
    response = requests.get(url)
    body=json.loads(response.text)
    assert response.status_code==200
    with open("test_deleyed.txt","w") as f:
        f.write(str(body))