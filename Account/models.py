from django.db import models

# Create your models here.

class User( models.Model ):
    username = models.CharField(max_length=20, unique=True)
    user_role = models.CharField (max_length=30)
    registered = models.BooleanField (default=False)
    class Meta:
        db_table="user_information"
        managed = False


class AccUser( models.Model ):
    username = models.CharField(max_length=20, unique=True)
    password=models.CharField(max_length=128)
    class Meta:
        db_table="auth_user"
        managed = False

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