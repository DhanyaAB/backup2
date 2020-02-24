from django.contrib.admin.utils import lookup_field
from django.shortcuts import render

from django import forms
from django.shortcuts import render,redirect
from django.template import RequestContext
from rest_framework.views import APIView
from .models  import student_details as student_detailsModel
from .serializers import studentSerializer
from .forms import studentForm
from django.shortcuts import HttpResponse
import re
import json
from django.core import serializers
from django.shortcuts import render_to_response

class student(APIView):
	lookup_field = 'id'
	serializer_class =studentSerializer

	def add(request):
		if request.method=='POST':
			College_name=request.POST['college_name']
			Name_student=request.POST['name']
			USN=request.POST['usn']
			Branch=request.POST['branch']
			student_de=student_detailsModel(College_name=College_name,Name_student=Name_student,USN=USN, Branch=Branch)
			student_de.save()
			return render(request, 'disp_de.html',  {})
		else:
			return render(request, 'insert.html',  {})


	def edit(request,id):
		form= student_detailsModel.objects.get(pk=id)
		return render(request, 'update.html', {"form": form})

	def update(request,id):

			form1 = student_detailsModel.objects.get(pk=id)
			form = studentForm(request.POST, instance=form1)

			if request.method == 'POST':
				if form.is_valid():
					form.save()
					return redirect('/complete/')
			else:
				return render(request, 'update.html', {"form": form1})



	def get(request):
		complete= student_detailsModel.objects.all()
		output_serializer= studentSerializer(complete,many=True)
		c= output_serializer.data[:]
		c=json.loads(json.dumps(c))
		print(type(c))
		return render(request,'disp_de.html',{"c":c})

	def getObject(request,id):
		complete = student_detailsModel.objects.filter(pk=id)
		output_serializer = studentSerializer(complete, many=True)
		c = output_serializer.data[:]
		c = json.loads(json.dumps(c))
		return render(request, 'disp_de.html', {"c": c})

	def delet_id(request,id):
		id1=id
		complete = student_detailsModel.objects.get(pk=id)
		if request.method=='POST':
			complete.delete()
			return redirect('/complete')
		else:

			return render(request, 'stu_delete.html', {'id': id1})

