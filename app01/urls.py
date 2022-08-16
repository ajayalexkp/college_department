from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_form, name='details_insert'),
    path('<int:id>/', views.department_form, name='details_update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('list/', views.department_list, name='list')
]