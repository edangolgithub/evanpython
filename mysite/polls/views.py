from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def hello(request):
    return HttpResponse("this is hello")    
def learn(request):
    return HttpResponse("i think i learned python")