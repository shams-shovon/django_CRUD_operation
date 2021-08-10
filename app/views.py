from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def create(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'app/create.html',context)