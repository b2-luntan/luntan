#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request , "index.html")

def add (request):
	return render(request , 'add.html')

def testjia(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def testjia2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def testhtml(request):
	return render(request , "home.html")