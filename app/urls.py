from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('custom-admin/', views.admin_panel, name='admin_panel'),
    path('custom-admin/projects/', views.admin_projects, name='admin_projects'),
    path('custom-admin/contacts/', views.admin_contacts, name='admin_contacts'),
    path('custom-admin/projects/edit/', views.admin_project_edit, name='admin_project_edit'),
    path('custom-admin/projects/delete/', views.admin_project_delete, name='admin_project_delete'),
]