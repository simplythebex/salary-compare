from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .serializers import UserSerializer
from rest_framework import permissions, viewsets


def index(request):
    return HttpResponse("Hello, world. You're at the salaries index.")


class UserListView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# class UserListView():
#     def get(self, _request):
#         users = User.objects.all()
#         serialized_users = UserSerializer(users, many=True)
#         return Response(serialized_users.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         request.data['owner'] = request.user.id
#         user_to_add = UserSerializer(data=request.data)
#         if user_to_add.is_valid():
#             user_to_add.save()
#             return Response(user_to_add.data, status=status.HTTP_201_CREATED)
#         return Response(user_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
# class UserDetailView():
#     def get_user(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise NotFound(detail="User not found.")

#     def get(self, _request, pk):
#         user = self.get_user(pk=pk)
#         serialized_user = UserSerializer(user)
#         return Response(serialized_user.data, status=status.HTTP_200_OK)

#     def delete(self, _request, pk):
#         user_to_delete = self.get_user(pk=pk)
#         user_to_delete.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk):
#         user_to_edit = self.get_user(pk=pk)
#         updated_user = UserSerializer(user_to_edit, data=request.data)
#         if updated_user.is_valid():
#             updated_user.save()
#             return Response(updated_user.data, status=status.HTTP_202_ACCEPTED)
#         return Response(updated_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)