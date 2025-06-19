from django.shortcuts import render, redirect
from .import dbconf
from django.contrib import messages
from bson import ObjectId
from datetime import datetime
# Create your views here.

def home(request):
    projects = dbconf.projects.find()
    return render(request, 'app/home.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            contact_data = {
                'id': str(ObjectId()),
                'name': name,
                'email': email,
                'message': message,
                'timestamp': datetime.now()
            }
            dbconf.Contact.insert_one(contact_data)
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill out all fields...')
    return render(request, 'app/contact.html')

def admin_panel(request):
    return render(request, 'app/admin/AdminPanel.html')

def admin_projects(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        github_link = request.POST.get('github_link')
        
        if title and description and github_link and project_id:
            ProjectData = {
                'id': project_id,
                'title': title,
                'description': description,
                'link': github_link,
            }
            dbconf.projects.insert_one(ProjectData)
            messages.success(request, 'Project added successfully!')
        else:
            messages.error(request, 'Please fill out all fields...')
    projects = dbconf.projects.find()
    return render(request, 'app/admin/AdminProjects.html', {'projects': projects})


def admin_project_edit(request):
    return render(request, 'app/admin/AdminProjectEdit.html') 

def admin_project_delete(request):
    return render(request, 'app/admin/AdminProjectDelete.html')

def admin_contacts(request):
    contacts = dbconf.Contact.find()
    return render(request, 'app/admin/AdminContacts.html', {'contacts': contacts})


