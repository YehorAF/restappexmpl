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

To get users you must send request with method `GET` to `http://127.0.0.1:8000/users/` or to get only one user `http://127.0.0.1:8000/users/{user_id}`
```python
response = requests.get("http://127.0.0.1:8000/users/")
print(response, response.text, response.headers)

response = requests.get("http://127.0.0.1:8000/users/5")
print(response, response.text, response.headers)
```

To update user send request with method `POST`, `PUT` or `PATCH` to `http://127.0.0.1:8000/users/{user_id}` with fields `username` or `description` and `Api-Key` in headers
```python
response = requests.post("http://127.0.0.1:8000/users/4", json={
    "username": "somename5",
    "description": "really nice description"
}, headers={"Api-Key": "DbPx6dVa3n-8AJuC14E1Tg"})
print(response, response.text, response.headers)
```

To delete user send request with method `DELETE` to `http://127.0.0.1:8000/users/{user_id}` with `Api-Key` in headers
```python
response = requests.delete(
    "http://127.0.0.1:8000/users/2",
    headers={"Api-Key": "E12OmV0QtjOeO_gakm0qDw"})
print(response, response.text, response.headers)
```

## Work with tasks
To create task send request with `POST` or `PUT` to `http://127.0.0.1:8000/users/{user_id}/tasks/` with fields `name`, `content`, `start_time` and `deadline`
```python
response = requests.post("http://127.0.0.1:8000/users/2/tasks/", json={
    "name": "make some task",
    "content": "i don't know what to do",
    "start_time": "2023-12-28 22:00:00",
    "deadline": "2023-12-29 22:00:00"
}, headers={"Api-Key": "E12OmV0QtjOeO_gakm0qDw"})
print(response, response.text, response.headers)
```

To get tasks - `http://127.0.0.1:8000/users/{user_id}/tasks/`
```python
response = requests.get(
    "http://127.0.0.1:8000/users/4/tasks/",
    headers={"Api-Key": "E12OmV0QtjOeO_gakm0qDw"})
print(response, response.text, response.headers)
```

To delete task - `http://127.0.0.1:8000/users/{user_id}/tasks/{task_id}`
```python
response = requests.delete(
    "http://127.0.0.1:8000/users/2",
    headers={"Api-Key": "E12OmV0QtjOeO_gakm0qDw"})
print(response, response.text, response.headers)
```
