from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('insert/',views.student.add ,name='add'),
    path('complete/',views.student.get,name='value'),
    path('complete/edit/<int:id>/',views.student.edit,name='by_id'),
    path('update/<int:id>/',views.student.update,name='id'),
    path('data/<int:id>/',views.student.getObject,name='id'),
    path('complete/delete/<int:id>/',views.student.delet_id,name='delete_id'),

]
