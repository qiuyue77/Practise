from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookOrder
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from django.db import connection

"""
聚合查询
"""
# test
# def index(request):
#    result = Book.objects.aggregate()
#    print(result)
#    print(f'SQL查询语句：{connection.queries[-1]}')
#    return HttpResponse("index")

# avg
# def index(request):
#    result = Book.objects.aggregate(price_avg=Avg("price"))
#    print(result)
#    print(connection.queries)
#    return HttpResponse("index")
#
#
# def index1(request):
#    result = Book.objects.aggregate(avg=Avg("bookorder__price"))

# aggregate 和 annotate
# def index(request):
#    #result = Book.objects.aggregate(avg=Avg("bookorder__price"))
#    books = Book.objects.annotate(avg=Avg("bookorder__price"))
#    for book in books:
#        print(f'{book.name}:{book.avg}')
#    print(connection.queries)
#
#    return HttpResponse("index2")


# Count
# def index(request):
#     # 查询书籍的种类
#     #result = Book.objects.aggregate(book_nums=Count("id"))
#     # 统计每本书的销量
#     books = Book.objects.annotate(book_nums = Count("bookorder"))
#     for book in books:
#         print(f"{book.name}:{book.book_nums}")
#     print(books)
#     print(connection.queries)
#     return HttpResponse("index")


# Max & Min
# def index(request):
#    #result = Author.objects.aggregate(max=Max("age"), min=Min("age"))
#    # 获取每个人图书售卖时最大价格以及最小价格
#    books = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
#    for book in books:
#       print(f"{book.name}:{book.max}:{book.min}")
#    print(connection.queries)
#    return HttpResponse("index")


# Sum
# def index(request):
# result = BookOrder.objects.aggregate(sum = Sum("price"))
# print(result)
# 每本书的销售总额
# books = Book.objects.annotate(sum=Sum("bookorder__price"))
# for book in books:
#    print(f'{book.name}:{book.sum}')
# 2020 销售总额
# result = BookOrder.objects.filter(create_time__year=2020).aggregate(sum = Sum('price'))
# print(result)
# 2020 每本书销售总额
# books = Book.objects.filter(bookorder__create_time__year=2020).annotate(sum=Sum('bookorder__price'))
# for book in books:
#    print(f'{book.name}:{book.sum}')
# print(connection.queries)
# return HttpResponse("index")

# F表达式
# def index(request):
#     result = Book.objects.update(price=F('price') + 10)
#     print(result)
#     print(connection.queries[-1])
#     return HttpResponse("index")


# Q表达式
def index(request):
    # books = Book.objects.filter(price__gte=100, rating__gte=4.85)
    # for book in books:
    #     print(book.name)
    books = Book.objects.filter(Q(price__lt=108) | Q(rating__lt=4))
    for book in books:
        print(book.name)
    print(f'SQL查询语句：{connection.queries[-1]}')
    return HttpResponse("index")

