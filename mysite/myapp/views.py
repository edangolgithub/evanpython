from django.shortcuts import render,HttpResponse
import datetime  
#importing loading from django template  
from django.template import loader  
# Create your views here.
def hello(request):
   return HttpResponse("this is hello2")

def gettime(request):
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse  

def templat(request):
   y= loader.get_template('index.html')
   name = {  
        'student':'rahul' ,
        'roll':'100'
    }  
   return HttpResponse(y.render(name))