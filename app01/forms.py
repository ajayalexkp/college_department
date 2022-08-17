from django.forms import ModelForm
from .models import Department, College


class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = ['college_name']
        labels = {
            'college_name': 'COLLEGE',
        }


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = ['college_name', 'department_name', 'head_of_department', 'tutor']
        labels = {
            'college_name': 'COLLEGE',
            'department_name': 'DEPARTMENT',
            'head_of_department': 'HEAD OF DEPARTMENT(HOD)',
            'tutor': 'TUTOR',
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['college_name'].empty_label = "Select"



