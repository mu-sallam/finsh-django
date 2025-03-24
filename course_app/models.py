from django.db import models

# Create your models here.
class Course(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    @classmethod
    def get_all_courses(cls):
        return cls.objects.all()