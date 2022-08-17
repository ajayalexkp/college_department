from django.shortcuts import render, redirect
from .forms import DepartmentForm, CollegeForm
from .models import *

# Create your views here.


def department_list(request):
    context = {'department_list': Department.objects.all(), 'clg_list': College.objects.all()}
    return render(request, 'list.html', context)


def department_form(request, id=0):
    if request.method == "GET":
        if id == 0:                                                                                     #insert_operation
            dept_form = DepartmentForm()
        else:                                                                                           #update_operation
            department = Department.objects.get(pk=id)
            dept_form = DepartmentForm(instance=department)

        return render(request, 'dept_form.html', {'dept_form': dept_form})
    else:
        if id == 0:
            dept_form = DepartmentForm(request.POST)
        else:
            department = Department.objects.get(pk=id)
            dept_form = DepartmentForm(request.POST, instance=department)
        if dept_form.is_valid():
            dept_form.save()
        return redirect('/list')


def college_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            clg_form = CollegeForm()
        else:
            college = College.objects.get(pk=id)
            clg_form = CollegeForm(instance=college)
        return render(request, 'clg_form.html', {'clg_form': clg_form})
    else:
        if id == 0:
            clg_form = CollegeForm(request.POST)
        else:
            college = College.objects.get(pk=id)
            clg_form = CollegeForm(request.POST, instance=college)
        if clg_form.is_valid():
            clg_form.save()
        return redirect('/list')


def delete(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('/list')


def clg_delete(request, id):
    college = College.objects.get(pk=id)
    college.delete()
    return redirect('/list')





