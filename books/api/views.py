from rest_framework import generics, mixins
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = 'books'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
