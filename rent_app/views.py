from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")
