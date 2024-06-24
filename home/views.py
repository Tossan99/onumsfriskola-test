from django.shortcuts import render
from .models import Document, Staff

def view_home(request):
    """
    View to render home page
    """
    context = {

    }

    return render(request, 'home/index.html', context)

def view_documents(request):
    """
    View to render documents and links page
    """
    documents = Document.objects.all()

    context = {
        "documents": documents,
    }

    return render(request, 'home/documents.html', context)

def view_about(request):
    """
    View to render about page
    """
    return render(request, 'home/about.html')


def view_staff(request):
    """
    View to render staff page
    """
    staffs = Staff.objects.all()

    context = {
        "staffs": staffs,
    }

    return render(request, 'home/staff.html', context)