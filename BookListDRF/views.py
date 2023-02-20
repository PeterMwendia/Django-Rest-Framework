from django.shortcuts import render
# Create your views here.

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


