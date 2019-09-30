from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>hello world<h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about(request, *args, **kwargs):
    my_context = {"text":"value", "int": 20, "list": [1,2,3,4]}
    return render(request, "about.html", my_context)