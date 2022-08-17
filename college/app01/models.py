from django.db import models

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=50)

    def __str__(self):
        return self.college_name


class Department(models.Model):
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)
    tutor = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
