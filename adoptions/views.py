from django.shortcuts import render, HttpResponse
from .models import Pet

# Create your views here.
def home(request):
    return HttpResponse('<P>home view</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>pet detail view with id {pet_id}</p>')
