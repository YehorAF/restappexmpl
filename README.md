# restappexmpl
Simple app to create users and tasks using django rest framework.

## Work with users
To create user you must send request in json format with fields `username` and `description`
Example:
```
import requests

response = requests.post("http://127.0.0.1:8000/users/", json={
    "username": "somename2",
    "description": "some shit"
})
print(response, response.text, response.headers)
```
