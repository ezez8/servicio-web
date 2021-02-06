from django.db import models

# Create your models here.

class BaseEntity(models.Model):
    status = models.CharField(max_length=1, choices=(('E','ENABLED'),('D','DISABLED')), default='ENABLED')
    created_date = models.DateTimeField()
    deleted_date = models.DateTimeField()

    class Meta:
        abstract = True

class Entity(BaseEntity):
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True 

class Faculty(Entity):
    pass

class School(Entity):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Section(Entity):
    uc = models.IntegerField()
    semester = models.IntegerField()
    type = models.CharField(max_length=1, choices=[('M','MANDATORY'),('E','ELECTIVE')])
    ht = models.FloatField()
    hp = models.FloatField()
    hl = models.FloatField()