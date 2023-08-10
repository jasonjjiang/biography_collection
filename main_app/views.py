from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Biography, Version
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
  # Get the versions the biography doesn't have
  # First, create a list of the version ids that the biography DOES have
  id_list = biography.versions.all().values_list('id')
  # Now we can query for versions whose ids are not in the list using exclude
  versions_biography_doesnt_have = Version.objects.exclude(id__in=id_list)
  status_form = StatusForm()
  return render(request, 'biographies/detail.html', {
    'biography': biography, 'status_form': status_form,
    # Add the versions to be displayed
    'versions': versions_biography_doesnt_have
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

class VersionList(ListView):
  model = Version

class VersionDetail(DetailView):
  model = Version

class VersionCreate(CreateView):
  model = Version
  fields = '__all__'

class VersionUpdate(UpdateView):
  model = Version
  fields = ['name', 'color']

class VersionDelete(DeleteView):
  model = Version
  success_url = '/Versions'

def assoc_version(request, biography_id, version_id):
  Biography.objects.get(id=biography_id).versions.add(version_id)
  return redirect('detail', biography_id=biography_id)

def unassoc_version(request, biography_id, version_id):
  Biography.objects.get(id=biography_id).versions.remove(version_id)
  return redirect('detail', biography_id=biography_id)