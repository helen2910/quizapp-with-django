from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
OPTIONS = (
    ("A","A"),
    ("B","B"),
    ("C","C"),
    ("D","D"),
)
class AppUser(AbstractUser):
    score = models.IntegerField(default=0)
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["-id"]
    
    def choices(self):
        return Choices.objects.filter(question=self)
        
    
class Choices(models.Model):
    # choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    option = models.CharField(max_length=1, choices=OPTIONS)
    is_correct = models.BooleanField(default=False)
    
