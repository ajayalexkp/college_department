from django.forms import ModelForm
from .models import Department


class CollegeForm(ModelForm):

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
        super(CollegeForm, self).__init__(*args, **kwargs)
        self.fields['college_name'].empty_label = "Select"
