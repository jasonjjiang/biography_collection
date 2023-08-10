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
  path('biographies/<int:biography_id>/assoc_version/<int:version_id>/', views.assoc_version, name='assoc_version'),
  path('biographies/<int:biography_id>/unassoc_version/<int:version_id>/', views.unassoc_version, name='unassoc_version'),
  path('versions/', views.VersionList.as_view(), name='versions_index'),
  path('versions/<int:pk>/', views.VersionDetail.as_view(), name='versions_detail'),
  path('versions/create/', views.VersionCreate.as_view(), name='versions_create'),
  path('versions/<int:pk>/update/', views.VersionUpdate.as_view(), name='versions_update'),
  path('versions/<int:pk>/delete/', views.VersionDelete.as_view(), name='versions_delete'),
]