from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class voter( models.Model ):
    username = models.CharField(max_length=20, unique=True)
    User_Role = models.CharField(max_length=30)
    User_Status=models.BooleanField(default=True)

    class Meta:
        db_table="user_information"
        managed = False
    def __str__(self):
        return self.username


class VotingModel(models.Model):
    username=models.CharField(max_length=20,unique=True)
    protocol = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    presentation_skill = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (15.0)])
    confidence = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    strategic_plane = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (20.0)])
    answering = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    Time_management  = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    certifcate = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    written_exam = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    oral_interview = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    Str_and_opra_plane = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (15.0)])
    Total_40 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (40.0)])
    Total_60 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (60.0)])
    Total_100 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])

    def __str__(self):
        return self.username


def StatuseDef():
    return False

class Voters(models.Model):
    username = models.CharField (max_length=20, unique=True)
    stat = models.BooleanField (default=False)
    cand1 = models.BooleanField (default=False)
    cand2 = models.BooleanField (default=False)
    cand3 = models.BooleanField (default=False)
    cand4 = models.BooleanField (default=False)
    cand5 = models.BooleanField (default=False)
    cand6 = models.BooleanField (default=False)
    cand7 = models.BooleanField (default=False)
    cand8 = models.BooleanField (default=False)
    cand9= models.BooleanField (default=False)
    cand10 = models.BooleanField (default=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table="vote_info"
        managed = False


class Election_Committe(models.Model):
    username = models.CharField(max_length=20,unique=True)
    stat = models.BooleanField(default=False)
    cand1 = models.BooleanField (default=False)
    cand2 = models.BooleanField (default=False)
    cand3 = models.BooleanField (default=False)
    cand4 = models.BooleanField (default=False)
    cand5 = models.BooleanField (default=False)
    cand6 = models.BooleanField (default=False)
    cand7 = models.BooleanField (default=False)
    cand8 = models.BooleanField (default=False)
    cand9 = models.BooleanField (default=False)
    cand10 = models.BooleanField (default=False)
    cand11 = models.BooleanField (default=False)
    cand12 = models.BooleanField (default=False)
    cand13 = models.BooleanField (default=False)
    cand14 = models.BooleanField (default=False)
    cand15 = models.BooleanField (default=False)
    cand16 = models.BooleanField (default=False)
    cand17 = models.BooleanField (default=False)
    cand18 = models.BooleanField (default=False)
    cand19 = models.BooleanField (default=False)
    cand20 = models.BooleanField (default=False)
    cand21 = models.BooleanField (default=False)
    cand22 = models.BooleanField (default=False)
    cand23 = models.BooleanField (default=False)
    cand24 = models.BooleanField (default=False)
    cand25 = models.BooleanField (default=False)
    cand26 = models.BooleanField (default=False)
    cand27 = models.BooleanField (default=False)
    cand28 = models.BooleanField (default=False)
    cand29 = models.BooleanField (default=False)
    cand30 = models.BooleanField (default=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table="election_committe"
        managed = False

class Users( models.Model ):
    username = models.CharField(max_length=20, unique=True)
    class Meta:
        db_table="user_information"
        managed = False
    def __str__(self):
        return self.username
