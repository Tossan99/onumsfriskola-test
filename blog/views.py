from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import SchoolClass


def view_all_school_classes(request):
    """ 
    Renders all school classes and posts
    """

    school_classes = SchoolClass.objects.all()

    context = {
        "school_classes": school_classes,
    }

    return render(request, "blog/school_classes.html", context)

def view_school_class(request, slug):
    """ 
    Renders a school class and it's related posts
    """

    school_classes = SchoolClass.objects.all()
    school_class = get_object_or_404(school_classes, slug=slug)

    context = {
        "school_class": school_class,
        "school_classes": school_classes,
    }

    return render(request, "blog/school_classes.html", context)
