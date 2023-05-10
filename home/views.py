from django.shortcuts import render
from .forms import RegistrantionForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'pages/home.html')

def register(request):
    form = RegistrantionForm()
    if request.method=='POST':
        form = RegistrantionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def error404(request, exception):
    return render(request,'pages/error.html')

def error500(request):
    return render(request,'pages/error.html')