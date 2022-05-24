from django.urls import path

from .views import *

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('journals/', JournalListAPIView.as_view()),
    path('journals/<int:pk>/', JournalDetailAPIView.as_view())
]