from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework import viewsets
from app.models import Todo
from app.serializers import TodoSerializers

class TodoViewsets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


