from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_form, name='details_insert'),
    path('college/', views.college_form, name='college_insert'),
    path('college/<int:id>/', views.college_form, name='college_update'),
    path('college/delete/<int:id>/', views.clg_delete, name='delete_college'),
    path('<int:id>/', views.department_form, name='details_update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('list/', views.department_list, name='list'),











    # path('college/', views.college_form, name='college_insert'),
    # path('college/<int:id>/', views.college_form, name='details_update'),
    # path('college/delete/<int:id>/', views.delete_college, name='delete_college'),
    # path('list/college', views.college_list, name='list_college')
]
