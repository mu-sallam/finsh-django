from django.db import models
from course_app.models import Course

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
