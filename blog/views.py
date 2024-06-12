from django.shortcuts import render

def view_blog(request):
    """
    View to render blog page
    """
    context = {

    }

    return render(request, 'blog/blog.html', context)
