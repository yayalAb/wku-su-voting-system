from django.db import models

# Create your models here.

class AnnounceModel(models.Model):
    Ann_By=models.CharField(max_length=20)
    Ann_Title = models.CharField (max_length=200)
    Ann_Dis=models.TextField(max_length=1000)
    Ann_Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Ann_Title




