from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    user_fname = models.CharField(max_length=50)
    user_lname=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=7)
    user_email=models.EmailField(max_length=100)
    user_phone=models.CharField(max_length=20)
    user_role=models.CharField(max_length=30)
    user_status = models.BooleanField (default=True)
    registered = models.BooleanField (default=False)
    user_fp=models.CharField(max_length=30)
    class Meta:
        db_table="user_information"
        managed = False
    def __str__(self):
        return self.username

class AnnounceModel(models.Model):
    Ann_By=models.CharField(max_length=20)
    Ann_Title = models.CharField (max_length=200)
    Ann_Dis=models.TextField(max_length=1000)
    Ann_Date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="announcement_announcemodel"
        managed = False

    def __str__(self):
        return self.Ann_Title

class ComplainModel(models.Model):
    to = (
        ("Admin", "Admin Group"),
        ("Committee", "Election Committee Group"),
    )
    com_id=models.AutoField(primary_key=True)
    comp_by=models.CharField(max_length=20)
    comp_dis = models.TextField (max_length=1000)
    comp_to=models.CharField(max_length=50, choices=to)
    comp_date=models.DateField(auto_now_add=True)
    class Meta:
        db_table="complain_complainmodel"
        managed = False

class Responsemodel(models.Model):
    com_id= models.ForeignKey(ComplainModel,on_delete=models.CASCADE)
    comp_response = models.TextField (max_length=1000)
    response_by = models.CharField(max_length=50)
    response_group = models.CharField (max_length=50)
    response_date = models.DateField (auto_now_add=True)
    class Meta:
        db_table="complain_response1"
        managed = False

class ScheduleModel(models.Model):
    action=models.CharField(max_length=200)
    Start_date = models.DateField()
    End_date=models.DateField()
    Scheduled_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.action
    class Meta:
        db_table="schedule_voting_day_schedulemodel"
        managed = False

class VotingModel(models.Model):
    username=models.CharField(max_length=20)
    protocol = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    presentation_skill = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (15.0)])
    confidence = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    strategic_plane = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (20.0)])
    answering = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    Time_management  = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    certifcate = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    written_exam = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    oral_interview = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (10.0)])
    Str_and_opra_plane = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (15.0)])
    Total_40 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])
    Total_60 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])
    Total_100 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])
    def __str__(self):
        return self.username
    class Meta:
        db_table="vote_votingmodel"
        managed = False

class notesModel(models.Model):
    noteID = models.CharField (max_length=20, default="1234")
    noteTitle =  models.CharField (max_length=100)
    noteContent= models.CharField (max_length=1000, null=True)
    createDateTime = models.DateField (auto_now_add=True)
    latestEditDateTime = models.DateField (auto_now_add=True)
    def __str__(self):
        return self.noteID
    class Meta:
        db_table="notesModel"
        managed = False

class Voters(models.Model):
    username = models.CharField (max_length=20, unique=True)
    stat = models.BooleanField (default=False)
    cand1 = models.BooleanField (default=False)
    cand2 = models.BooleanField (default=False)
    cand3 = models.BooleanField (default=False)
    cand4 = models.BooleanField (default=False)
    cand5 = models.BooleanField (default=False)
    cand6 = models.BooleanField (default=False)

    def __str__(self):
        return self.username
    class Meta:
        db_table = "vote_info"
        managed = False


class CampaignModel(models.Model):
    camp_by=models.CharField(max_length=20)
    camp_title = models.CharField(max_length=200)
    camp_dis = models.TextField (max_length=3000)
    camp_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.camp_title
    class Meta:
        db_table="campaign_campaign"
        managed = False