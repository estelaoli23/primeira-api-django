from rest_framework import viewsets
from books.api.serializers import BooksSerializer
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    seralizer_class = BooksSerializer
    queryset = models.Books.objects.all()