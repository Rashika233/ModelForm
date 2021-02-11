from django.shortcuts import render

# Create your views here.

from . forms import EmployeeForm

def home_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form' : form
    }
    return render(request, 'home.html', context)