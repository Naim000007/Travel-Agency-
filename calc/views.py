from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDict

# Create your views here.
def home(request):
    return render (request,'home.html',{'name':'Naim'})

def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = val1+ val2
    return render (request,'restul.html', {'result':res})