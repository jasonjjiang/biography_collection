from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('biographies/', views.biographies_index, name='index'),
  path('biographies/<int:biography_id>/', views.biographies_detail, name='detail'),

]

