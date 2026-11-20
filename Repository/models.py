from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionsDb(models.Model):
    
    title = models.CharField(max_length=200)
    LANGUAGE_CHOICES = (
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript")
    )
    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")

    DIFFICULTY_LEVELS = (
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )
    difficulty_level = models.CharField(max_length=100,choices=DIFFICULTY_LEVELS,default="easy")

    topic = models.CharField(max_length =100)

    notes = models.TextField()

    sample_input = models.TextField()

    sample_output = models.TextField()

    published_date = models.DateTimeField(auto_now_add =True)

    is_active = models.BooleanField(default=True)



class SubmissionsDb(models.Model):

    question_id = models.IntegerField()

    answer = models.TextField()

    points = models.PositiveIntegerField(null=True,blank=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="submissions")

    submission_date = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(null=True,blank=True)