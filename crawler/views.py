from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to solving issues")

def create_year_link():
    return False

def create_file_link():
    return False