from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Biography, Version
from .forms import StatusForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def biographies_index(request):
  biographies = Biography.objects.filter(user=request.user)
  # You could also retrieve the logged in user's biographies like this
  # biographies = request.user.biography_set.all()
  return render(request, 'biographies/index.html', { 'biographies': biographies })

@login_required
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

class BiographyCreate(LoginRequiredMixin, CreateView):
  model = Biography
  fields = '__all__'

class BiographyUpdate(LoginRequiredMixin, UpdateView):
  model = Biography
  fields = ['title', 'author', 'status']

class BiographyDelete(LoginRequiredMixin, DeleteView):
  model = Biography
  success_url = '/biographies'

def add_status(request, biography_id):
  # Create a ModelForm instance using the data that was submitted in the form
  form = StatusForm(request.POST)
  # Validate the form
  if form.is_valid():
    # We want a model instance, but we can't save to the db yet because we have not assigned the biography_id FK.
    new_status = form.save(commit=False)
    new_status.biography_id = biography_id
    new_status.save()
  return redirect('detail', biography_id=biography_id) 

class VersionList(LoginRequiredMixin, ListView):
  model = Version

class VersionDetail(LoginRequiredMixin, DetailView):
  model = Version

class VersionCreate(LoginRequiredMixin, CreateView):
  model = Version
  fields = '__all__'

class VersionUpdate(LoginRequiredMixin, UpdateView):
  model = Version
  fields = ['name', 'color']

class VersionDelete(LoginRequiredMixin, DeleteView):
  model = Version
  success_url = '/Versions'

@login_required
def assoc_version(request, biography_id, version_id):
  Biography.objects.get(id=biography_id).versions.add(version_id)
  return redirect('detail', biography_id=biography_id)

@login_required
def unassoc_version(request, biography_id, version_id):
  Biography.objects.get(id=biography_id).versions.remove(version_id)
  return redirect('detail', biography_id=biography_id)

def form_valid(self, form):
  # Assign the logged in user (self.request.user)
  form.instance.user = self.request.user  # form.instance is the biography
    # Let the CreateView do its job as usual
  return super().form_valid(form)  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)