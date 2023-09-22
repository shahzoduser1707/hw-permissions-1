from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import BookModel
from .serializer import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import OwnerPermission
# Create your views here.

class ListBookApiView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)


class DetailUpdateDestroyBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,OwnerPermission)