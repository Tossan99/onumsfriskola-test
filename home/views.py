from django.shortcuts import render

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
    context = {

    }

    return render(request, 'home/documents.html', context)
