from django.shortcuts import render
from .models import Biography

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def biographies_index(request):
  biographies = Biography.objects.all()
  return render(request, 'biographies/index.html', {
    'biographies': biographies
  })

def biographies_detail(request, biography_id):
  biography = Biography.objects.get(id=biography_id)
  return render(request, 'biographies/detail.html', {
    'biography': biography
  })