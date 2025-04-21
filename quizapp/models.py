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
    username =models.CharField(max_length=255, null=True, blank=True,unique=True)    
    score = models.IntegerField(default=0)
    # num_of_correct_choices = models.IntegerField(default=0)
    has_submitted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    


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
    
    class Meta:
        verbose_name_plural = "Choices"
