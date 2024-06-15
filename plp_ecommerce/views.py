from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color: purple;'>Our web progress</h1>")