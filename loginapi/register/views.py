from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serilaizer import UsersSerializer
from register.models import  Users

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from register.models import Loginapi
from .serilaizer import LoginapiSerializer
from rest_framework import permissions

class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer



class CreateUserAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer



class RegisterDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, register_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Loginapi.objects.get(id=register_id, user = user_id)
        except Loginapi.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, register_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        register_instance = self.get_object(register_id, request.user.id)
        if not register_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LoginapiSerializer(register_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, register_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        register_instance = self.get_object(register_id, request.user.id)
        if not register_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = LoginapiSerializer(instance = register_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, register_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        register_instance = self.get_object(register_id, request.user.id)
        if not register_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        register_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )