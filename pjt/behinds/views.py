from django.shortcuts import render, redirect
from .forms import BehindForm
from .models import Behind


# Create your views here.
def index(request):
    behinds = Behind.objects.all()
    context = {
        'behinds': behinds,
    }
    return render(request, 'behinds/index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')
        behind_values = {
            'title': title,
            'content': content,
            'csrfmiddlewaretoken': csrfmiddlewaretoken
        }
        form = BehindForm(behind_values)
        if form.is_valid():
            behind = form.save(commit=False)
            # behind.user = request.user
            behind.save()
            return redirect('behinds:index')
        return render(request, 'behinds/create.html')
    else:
        return render(request, 'behinds/create.html')
