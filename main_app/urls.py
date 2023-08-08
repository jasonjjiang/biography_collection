from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('biographies/', views.biographies_index, name='index'),
  path('biographies/<int:biography_id>/', views.biographies_detail, name='detail'),
  path('biographies/create/', views.BiographyCreate.as_view(), name='biographies_create'),
  path('biographies/<int:pk>/update/', views.BiographyUpdate.as_view(), name='biographies_update'),
  path('biographies/<int:pk>/delete/', views.BiographyDelete.as_view(), name='biographies_delete'),
  path('biographies/<int:biography_id>/add_status/', views.add_status, name='add_status'),
]


