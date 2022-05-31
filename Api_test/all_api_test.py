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
    # data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    response = requests.get(url)
    token = json.loads(response.text)
    assert response.status_code==200
    print(response)
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content
    # f = open("list_User.txt", "a")
    # f.write(response)
    # f.close()
    