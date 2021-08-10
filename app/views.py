from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def create(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'app/create.html',context)