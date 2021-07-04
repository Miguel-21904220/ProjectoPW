from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Formulario(models.Model):
    primeiroNome = models.CharField(max_length=30)
    ultimoNome = models.CharField(max_length=30)
    idade = models.DateField()
    email = models.EmailField(max_length=50)
    commentario = models.CharField(max_length=500)

    def __str__(self):
        return self.email

class Quiz(models.Model):
    
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=CASCADE, default="", editable=False, null=True)
    
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    answer5 = models.CharField(max_length=100)
    answer6 = models.CharField(max_length=100)
    answer7 = models.CharField(max_length=100)
    answer8 = models.CharField(max_length=100)
    answer9 = models.CharField(max_length=100)
    answer10 = models.CharField(max_length=100)
    
    def __str__(self):
        return f"User : {self.created_by}"
    
class Comment(models.Model):

    name = models.CharField(max_length=32)
    comment = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.comment