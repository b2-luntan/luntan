#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse(u"欢迎光临，帅气的光的页面")

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