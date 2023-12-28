from rest_framework import status, decorators, views
from rest_framework.request import Request
from rest_framework.response import Response

from datetime import datetime
import secrets
import logging

from .models import User, Task
from .serializers import UserSerializer, TaskSerializer, UserCreationSerializer


def get_users(request: Request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    

def create_user(request: Request):
    try:
        api_key = secrets.token_urlsafe(16)
        serializer = UserCreationSerializer(
            data=request.data | {"api_key": api_key})
        if not serializer.is_valid():
            raise ValueError(str(serializer.error_messages))
        serializer.save()
        response = Response(serializer.data, headers={"Api-Key": api_key})
    except Exception as ex_:
        response = Response(
            {"error": True, "description": f"cannot create user: {ex_}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


@decorators.api_view(["GET", "POST", "PUT"])
def users(request: Request):
    if request.method == "GET":
        return get_users(request)
    elif request.method in ["POST", "PUT"]:
        return create_user(request)
    

def get_user_by_id(request: Request, user_id: int):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        response = Response(serializer.data)
    except:
        response = Response(
            {"error": True, "descrition": "not such user"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


def update_user(request: Request, user_id: int):
    api_key = request.META.get("HTTP_API_KEY")
    try:
        user = User.objects.filter(id=user_id, api_key=api_key)
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValueError(str(serializer.error_messages))
        user.update(**serializer.data)
        response = Response(
            {"error": False, "descrition": "user was updated"},
        )
    except Exception as ex_:
        response = Response(
            {"error": True, "descrition": f"cannot update user: {ex_}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


def delete_user(request: Request, user_id: int):
    api_key = request.META.get("HTTP_API_KEY")
    try:
        User.objects.get(id=user_id, api_key=api_key).delete()
        response = Response(
            {"error": False, "descrition": "user was deleted"},
        )
    except Exception as ex_:
        response = Response(
            {"error": True, "descrition": f"cannot delete user {ex_}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


@decorators.api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def user(request: Request, user_id: int):
    if request.method == "GET":
        return get_user_by_id(request, user_id)
    elif request.method in ["POST", "PUT", "PATCH"]:
        return update_user(request, user_id)
    elif request.method == "DELETE":
        return delete_user(request, user_id)


def get_tasks(request: Request, user_id: int):
    api_key = request.META.get("HTTP_API_KEY")
    try:
        User.objects.get(id=user_id, api_key=api_key)
        tasks = Task.objects.filter(user_id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        response = Response(serializer.data)
    except:
        response = Response(
            {"error": True, "descrition": "cannot get tasks"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


def create_task(request: Request, user_id: int):
    api_key = request.META.get("HTTP_API_KEY")
    try:
        User.objects.get(id=user_id, api_key=api_key)
        data = request.data.copy() | {"user_id": user_id}
        serializer = TaskSerializer(data=data)
        if not serializer.is_valid():
            raise ValueError(str(serializer.error_messages))
        serializer.save()
        response = Response(data=serializer.data)
    except Exception as ex_:
        response = Response(
            {"error": True, "descrition": f"cannot create task: {ex_}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response


@decorators.api_view(["GET", "POST", "PUT"])
def tasks(request: Request, user_id: int):
    if request.method == "GET":
        return get_tasks(request, user_id)
    elif request.method in ["POST", "PUT"]:
        return create_task(request, user_id)


@decorators.api_view(["DELETE"])
def delete_task(request: Request, user_id: int, task_id: int):
    api_key = request.META.get("HTTP_API_KEY")
    try:
        User.objects.get(id=user_id, api_key=api_key)
        Task.objects.get(user_id=user_id, id=task_id).delete()
        response = Response(
            {"error": False, "descrition": "task was deleted"},
        )
    except Exception as ex_:
        response = Response(
            {"error": True, "descrition": f"cannot delete task: {ex_}"},
            status=status.HTTP_400_BAD_REQUEST
        )
    return response