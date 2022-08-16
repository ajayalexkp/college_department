from django.shortcuts import render, redirect
from .forms import CollegeForm
from .models import *

# Create your views here.


def department_list(request):
    context = {'department_list': Department.objects.all()}
    return render(request, 'list.html', context)


def department_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CollegeForm()
        else:
            department = Department.objects.get(pk=id)
            form = CollegeForm(instance=department)
        return render(request, 'form.html', {'form': form})
    else:
        if id == 0:
            form = CollegeForm(request.POST)
        else:
            department = Department.objects.get(pk=id)
            form = CollegeForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        return redirect('/list')


def delete(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('/list')
