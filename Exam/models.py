from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class exam_model(models.Model):
    ans = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),

    )
    question= models.TextField (max_length=1000)
    choiceA = models.TextField (max_length=1000)
    choiceB = models.TextField (max_length=1000)
    choiceC = models.TextField (max_length=1000)
    choiceD = models.TextField (max_length=1000, default="All")
    choiceE = models.TextField (max_length=1000,default="None")
    answer = models.CharField (max_length=1, choices=ans)
    User_answer = models.CharField (max_length=50,blank=True)


class ExamresultModel(models.Model):
    username=models.CharField(max_length=20,unique=True)
    written_exam = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    Total_40 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (40.0)])
    Total_100 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])
    def __str__(self):
        return self.username
    class Meta:
        db_table="vote_votingmodel"
        managed = False