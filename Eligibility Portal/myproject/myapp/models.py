from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    email_id = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    college = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    div = models.CharField(max_length=30)   
    role=models.CharField(max_length=20)
    
    
    class Meta:
        db_table = "Students"

class Aptitude(models.Model):
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.EmailField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    
    
    class Meta:
        db_table = "Aptitude"
        
class Technical(models.Model):
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.EmailField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    
    
    class Meta:
        db_table = "Technical"        
        
class Listquestions(models.Model):
    qid=models.CharField(max_length=50)
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.EmailField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct= models.CharField(max_length=500,default="A")
    qtype=models.CharField(max_length=100,default="apti")
    
    class Meta:
        db_table = "Listquestions"          
        
class quizattempt(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
  
    class Meta:
        db_table = "quizattempt"          
        
        
class Finalresults(models.Model):
    sid=models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    year = models.CharField(max_length=100)
    college= models.CharField(max_length=100)
    branch= models.CharField(max_length=100)
    div= models.CharField(max_length=100)
    strtime= models.CharField(max_length=100)
    endtime= models.CharField(max_length=100)
    marks= models.CharField(max_length=100)
    
    class Meta:
        db_table = "Finalresults"          