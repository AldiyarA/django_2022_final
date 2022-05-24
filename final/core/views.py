from django.shortcuts import render
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import generics, permissions, status


# Create your views here.

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )


class BookListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JournalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

