from django.db import models
# Create your models here.



class People(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    birthday=models.DateField(auto_now=True)

    class Meta:
        db_table='people'

class Father(models.Model):
    name=models.CharField(max_length=32)
    people=models.ForeignKey(to=People,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table='father'

class Person(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=0)
    height=models.FloatField(max_length=32)

    class Meta:
        db_table='person'


class Teacher(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=32)
    person=models.ManyToManyField(to=Person)

    class Meta:
        db_table='teacher'