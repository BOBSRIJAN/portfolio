from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('custom-admin/', views.admin_panel, name='admin_panel'),
    path('custom-admin/projects/', views.admin_add_projects, name='admin_add_projects'),
    path('custom-admin/contacts/', views.admin_contacts, name='admin_contacts'),
    path('custom-admin/projects/edit/', views.admin_project_edit, name='admin_project_edit'),
    path('custom-admin/projects/edit/<str:id>/', views.admin_project_edit_form, name='admin_project_edit_form'),
    path('custom-admin/projects/delete/', views.admin_project_delete, name='admin_project_delete'),
    path('custom-admin/logout/', views.logout_view, name='logout_view'),
]