from django.http import HttpResponse
import csv


def index(request):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition']= "attachment;filename=abc.csv"
   writer = csv.writer(response)
   writer.writerow(['username','age'])
   writer.writerow(['jqiu','18'])
   return response
