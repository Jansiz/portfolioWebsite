from cProfile import label
from django.shortcuts import render
from .models import project, skills
from .form import contactForm
# Create your views here.

def homepage(request):

    form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            form = contactForm()
    #pull the html template 
    return render(request=request, template_name="main/index.html",
    #pull model
    context={"projects": project.objects.all, "form": form, "skills": skills.objects.all})

def privacy(request):
#pull the html template 
    return render(request=request, template_name="main/privacy.html",
)

def terms(request):
#pull the html template 
    return render(request=request, template_name="main/terms.html",
)

def licenses(request):
#pull the html template 
    return render(request=request, template_name="main/licenses.html",
)

def credits(request):
#pull the html template 
    return render(request=request, template_name="main/credits.html",
)
