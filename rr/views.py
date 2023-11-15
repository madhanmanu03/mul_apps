from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sanju(request):
    return render(request,'sanju.html')


def padikal(request):
    return HttpResponse("<h1>padikal</h1>")