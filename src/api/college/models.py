from django.db import models
from django.utils.timezone import now

# Create your models here.

class BaseEntity(models.Model):
    status = models.CharField(max_length=1, choices=(('E','ENABLED'),('D','DISABLED')), default='E')
    created_date = models.DateTimeField(default=now())
    deleted_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True

class Entity(BaseEntity):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, default='')

    class Meta:
        abstract = True 

class Faculty(Entity):
    pass

class School(Entity):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Section(Entity):
    uc = models.IntegerField()
    semester = models.IntegerField()
    type = models.CharField(max_length=1, choices=[('M','MANDATORY'),('E','ELECTIVE')], default='M')
    ht = models.FloatField()
    hp = models.FloatField()
    hl = models.FloatField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Person(BaseEntity):
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)

class Enrollment(BaseEntity):
    type = models.CharField(max_length=1, choices=[('S','STUDENT'),('T','TEACHER')], default='S')
    section = models.ManyToManyField(Section) 
    
