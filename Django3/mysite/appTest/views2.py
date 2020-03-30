from builtins import print

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookOrder
from django.db.models.manager import Manager
from django.db.models import F
from django.db.models.functions import Lower
from django.db import connection

"""
Queryset_API
"""

# test
# def index(request):
#    result = Book.objects.aggregate()
#    print(result)
#    print(f'SQL查询语句：{connection.queries[-1]}')
#    return HttpResponse("index")

# select_related()
#def index(request):
#   # books = Book.objects.all()
#   books = Book.objects.select_related('author')
#   for book in books:
#      print(book.author.name)
#   print(f'SQL查询语句：{connection.queries}')
#   return HttpResponse("index")

# prefetch_related()
def index(request):
   # books = Book.objects.all()
   books = Book.objects.prefetch_related('bookorder_set')
   for book in books:
       print('='*30)
       print(book.name)
       orders = book.bookorder_set.all()
       for order in orders:
           print(order.id)
   print(f'SQL查询语句：{connection.queries}')
   return HttpResponse("index")
