from django.db import models

# Create your models here.
class User( models.Model ):
    username = models.CharField(max_length=20, unique=True)
    user_fname = models.CharField(max_length=50)
    user_lname=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=7)
    user_email=models.EmailField(max_length=100)
    user_phone=models.CharField(max_length=20)
    user_role = models.CharField(max_length=30)
    user_status=models.BooleanField(default=True)
    registered = models.BooleanField(default=False)
    image = models.ImageField (default="profile1.png", null=True, blank=True)
    key = models.CharField (max_length=30, default="000000", blank=True)
    user_fp=models.CharField(max_length=30,default="000000" ,blank=True)
    class Meta:
        db_table="user_information"
        managed = False
    def __str__(self):
        return self.username

class Voter(models.Model):
    username = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table="vote_info"
        managed = False

class candidate (models.Model):
    username = models.CharField (max_length=20, unique=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table="vote_votingmodel"
        managed = False



class Election_Committe(models.Model):
    username = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table="election_committe"
        managed = False

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title



