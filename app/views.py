from django.shortcuts import render,redirect
from . import dbconf
from django.contrib import messages
from bson import ObjectId
# Create your views here.

def home(request):
    
    return render(request, 'app/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

    return render(request, 'app/contact.html')


def admin_panel(request):
    return render(request, 'app/admin/AdminPanel.html')

def admin_projects(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        github_link = request.POST.get('github_link')
        
        if title and description and image and github_link and project_id:
            project_data = {
                'id': project_id,
                'title': title,
                'description': description,
                'image': image,
                'link': github_link
            }
    #         if project_id:  # Update existing project
    #             ProjectDocument.objects.filter(id=ObjectId(project_id)).update(project=project_data)
    #             messages.success(request, 'Project updated successfully!')
    #         else:  # Create new project
    #             ProjectDocument.objects.create(project=project_data)
    #             messages.success(request, 'Project added successfully!')
    #     else:
    #         messages.error(request, 'Please fill out all fields.')
    #     return redirect('admin_projects')
    
    # projects = ProjectDocument.objects.all()
    projects = dbconf.projects.find()
    return render(request, 'app/admin/AdminProjects.html', {'projects': projects})


def admin_contacts(request):
    contacts = dbconf.Contact.find()
    return render(request, 'app/admin/AdminContacts.html', {'contacts': contacts})


