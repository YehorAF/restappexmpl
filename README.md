# restappexmpl
Simple app to create users and tasks using django rest framework.

## Work with users
To create user you must send request in json format with fields `username` and `description`
```python
import requests

response = requests.post("http://127.0.0.1:8000/users/", json={
    "username": "somename2",
    "description": "some"
})
print(response, response.text, response.headers)
```
It returns fields `username`, `description`, `id` and `api_key`

To get users you must send request with method `GET` to url `http://127.0.0.1:8000/users/` or to get only one user `http://127.0.0.1:8000/users/{user_id}`
```python
response = requests.get("http://127.0.0.1:8000/users/")
print(response, response.text, response.headers)

response = requests.get("http://127.0.0.1:8000/users/5")
print(response, response.text, response.headers)
```

To update user send request with method `POST`, `PUT` or `PATCH` to url `http://127.0.0.1:8000/users/{user_id}` with fields `username` or `description` and `Api-Key` in headers
```python
response = requests.post("http://127.0.0.1:8000/users/4", json={
    "username": "somename5",
    "description": "really nice description"
}, headers={"Api-Key": "DbPx6dVa3n-8AJuC14E1Tg"})
