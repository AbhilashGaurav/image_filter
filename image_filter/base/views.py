from django.shortcuts import render
from .forms import ImageForm, DocumentForm
from .models import Image
from django.http import HttpResponse
import io
from django import forms

def home(request):
  if request.method == "POST":
    form = ImageForm(request.POST, request.FILES)
  
  # title = form.title
  if form.is_valid():
    form.save()
  form = ImageForm()
  img = Image.objects.all()
  return render(request, 'myapp/home.html', {'img':img, 'form':form})