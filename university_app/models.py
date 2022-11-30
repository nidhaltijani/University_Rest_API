#import enum
#from random import choices
from django.db import models
#from django.forms import CharField
#from datetime import date
from django.utils import timezone
#import enum
#import datetime
# Create your models here.

class University(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False,default='')
    location=models.CharField(max_length=30,null=False,blank=False,default='')
    class Meta:
        db_table='University'


class Module(models.Model):
    class semesters(models.TextChoices):
        semestre1='S1','premier semetre'
        semestre2='S2','deuxieme semestre'
    name=models.CharField(max_length=70,null=False,blank=False,default='')
    nbHours=models.DecimalField(max_digits=4,decimal_places=2,default=21.0) # max digits  4 dedans 2 aprs la virgule
    semester=models.CharField(choices=semesters.choices,default=semesters.semestre1,max_length=150) # comme level
    coef=models.FloatField(default=1.0)
    credit=models.IntegerField(default=2)
    class Meta:
        db_table='Module'


class Person(models.Model):
    #id=models.IntegerField(max_length=8,default=0)
    name=models.CharField(max_length=70,null=False,blank=False,default='')
    familyName=models.CharField(max_length=70,null=False,blank=False,default='')
    birthDay=models.DateField(null=True,blank=True)#default=date(2004,1,1))
    email=models.EmailField(null=False,blank=False,max_length=100,default='example@xyz.com')

    class Meta:
        ordering=['name','familyName']
        abstract=True



class Teacher(Person):
    class grades(models.TextChoices):
        doctorant=('dr','doctorant')
        recrute=('rec','recrute')
        directeur=('dir','director')
        professor=('prof','professor')
    
    grade=models.CharField(choices=grades.choices,default=grades.doctorant,max_length=100)
    teacherModule=models.ManyToManyField(Module,through='TeacherModules',through_fields=('teacher','module'))
    nbHours=models.DecimalField(max_digits=4,decimal_places=2,default=21.0) # max digits  4 dedans 2 aprs la virgule
    #float field mandhesh params kyma decimal field
    class Meta:
        db_table='Teacher'


class TeacherModules(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    year=models.PositiveIntegerField(default=timezone.now().year)
    nbHours=models.DecimalField(max_digits=4,decimal_places=2,default=21.0) # max digits  4 dedans 2 aprs la virgule
    class Meta:
        db_table='TeacherModules'



class Group(models.Model):
    class levels(models.TextChoices):
        premiere = 'L1','premiere annee'
        deuxieme = 'L2','deuxieme annee'
        troisieme = 'L3','troisieme annee'
        premiere_master = 'M1','premiere master'
        deuxieme_master = 'M2','deuxieme master'
    name=models.CharField(max_length=70,null=False,blank=False,unique=True,default='')
    nbStudents=models.PositiveIntegerField(default=1)
    # fel mail ken nheb nhot null and blank false lezm default valide mail
    email=models.EmailField(null=False,blank=False,default='nom_du_groupe@xyz.com',max_length=100)
    speciality=models.CharField(null=False,blank=False,max_length=50,default='BI')
    level=models.CharField(max_length=20,choices=levels.choices,default=levels.premiere)
    # * à * entre modules et grp
    study=models.ManyToManyField(Module)
    class Meta:
        db_table='Group'


class address(models.Model):
    street = models.CharField(max_length=30,null=False,blank=False,verbose_name='Street Name',default='')
    city=models.CharField(max_length=30,null=False,blank=False,default='')
    adrs=models.CharField(max_length=35,null=False,blank=False,default='')
    zip_code=models.IntegerField(null=False,blank=False,default=0000)
    class Meta:
        db_table='Address'

#date a verifier si un prob occ
class listOfAbs(models.Model):
    date=models.DateField(null=True,blank=True)#,default=timezone.now().date) 
    motif=models.CharField(default='',max_length=100)
    justification=models.CharField(default='',max_length=100)
    class Meta:
        db_table='ListOfAbs'

class Student(Person):
    class states(models.TextChoices):
        present = ('pre','present student')
        absent = ('abs','absent student')
        delayed = ('del','delayed student')
        excluded = ('exc','excluded student')
    class situations(models.TextChoices):
        new = ('new','new student')
        repeating = ('rep','repeating student')
        derogatory = ('dero','derogatory student')
        other = ('oth','other student')
    photo=models.ImageField(upload_to='photos/students')
    state=models.CharField(max_length=20,choices=states.choices,default=states.present)
    situation=models.CharField(max_length=20,choices=situations.choices,default=situations.new)
    #relation 1 a plusieur entre student et univ
    univ=models.ForeignKey(University,on_delete=models.CASCADE)
    # 1 à * student et grp
    grp=models.ForeignKey(Group,null=True,blank=True,on_delete=models.CASCADE)
    # 1 à  1 student et adrs
    adrs=models.OneToOneField(address,on_delete=models.CASCADE)#,primary_key=True)
    class Meta:
        db_table='Student'
