from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
   return HttpResponse("this is hello2")
