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
