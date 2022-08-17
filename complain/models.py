from django.db import models

# Create your models here.

class ComplainModel(models.Model):
    to = (
        ("Admin", "Admin Group"),
        ("Committee", "Election Committee Group"),
    )
    com_id=models.AutoField(primary_key=True)
    comp_by=models.CharField(max_length=20)
    comp_dis = models.TextField (max_length=1000)
    comp_to=models.CharField(max_length=50, choices=to)
    comp_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="complain_complainmodel"
        managed = False


class Responsemodel(models.Model):
    com_id= models.ForeignKey(ComplainModel,on_delete=models.CASCADE)
    comp_response = models.TextField (max_length=1000)
    response_by = models.CharField(max_length=50)
    response_group = models.CharField (max_length=50)
    response_date = models.DateTimeField (auto_now_add=True)
    class Meta:
        db_table="complain_response1"
        managed = False

