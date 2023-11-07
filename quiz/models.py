


from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    allowed_time = models.PositiveIntegerField(default=60)  # Time in seconds

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
