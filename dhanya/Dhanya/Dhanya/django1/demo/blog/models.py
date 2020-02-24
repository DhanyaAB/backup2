from django.db import models

# Create your models here.
from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class student_details(models.Model):
    College_name = models.CharField(max_length=100)
    Name_student = models.CharField(max_length=100)
    USN = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)

    def __str__(self):
         return "collage_name:"+ self.College_name+    "student_name:" +self.Name_student+   "USN:" +self.USN+   "Branch;" + self.Branch






