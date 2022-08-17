from django.db import models

# Create your models here.

class ScheduleModel(models.Model):
    action=models.CharField(max_length=200)
    Start_date = models.DateField()
    End_date=models.DateField()
    Scheduled_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.action
