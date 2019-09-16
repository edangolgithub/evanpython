from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from myapp.forms import StuForm  

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   print 
   return HttpResponse(text)

def index(request):
   #return render(request, "myapp/templates/index.html", {})
   template = loader.get_template('index.html') # getting our template  
   name={'ram':'shyam'}
   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  

def frm(request):  
    stu = StuForm()  
    return render(request,"form.html",{'form':stu})  