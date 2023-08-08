from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Biography
from .forms import StatusForm

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
  status_form = StatusForm()
  return render(request, 'biographies/detail.html', {
    'biography': biography, 'status_form': status_form
  })

class BiographyCreate(CreateView):
  model = Biography
  fields = '__all__'

class BiographyUpdate(UpdateView):
  model = Biography
  fields = ['title', 'author', 'status']

class BiographyDelete(DeleteView):
  model = Biography
  success_url = '/biographies'

def add_status(request, biography_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = StatusForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # cat_id FK.
    new_status = form.save(commit=False)
    new_status.biography_id = biography_id
    new_status.save()
  return redirect('detail', biography_id=biography_id) 