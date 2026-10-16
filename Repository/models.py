from django.db import models

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