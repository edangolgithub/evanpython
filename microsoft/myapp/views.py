from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   print 
   return HttpResponse(text)

def index(request):
   #return render(request, "myapp/templates/index.html", {})
   template = loader.get_template('index.html') # getting our template  
   return HttpResponse(template.render())       # rendering the template in HttpResponse  
  