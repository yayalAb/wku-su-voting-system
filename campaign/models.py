from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class CampaignModel(models.Model):
    camp_by=models.CharField(max_length=20)
    camp_title = models.CharField(max_length=200)
    camp_dis = models.TextField (max_length=3000)
    camp_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.camp_title
    class Meta:
        db_table="campaign_campaign"
        managed = False

class  campaign_video(models.Model):
    username = models.CharField (max_length=20)
    video_dis = models.TextField(max_length=1000)
    video_file=models.FileField(upload_to='campaign_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    approval=models.BooleanField(default=False)

class  evaluation_video(models.Model):
    username = models.CharField (max_length=20, unique=True)
    video_dis = models.TextField(max_length=1000)
    video_file=models.FileField(upload_to='evaluation_videos',validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'M4P'])])
    approval = models.BooleanField (default=False)

class  fileUploading(models.Model):
    username = models.CharField (max_length=20)
    file_dis = models.TextField(max_length=1000,blank=True)
    certificate_file=models.FileField(upload_to='certificate',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    approval = models.BooleanField (default=False)

class VotingModel(models.Model):
    username=models.CharField(max_length=20,unique=True)
    certifcate = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (5.0)])
    Total_40 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (40.0)])
    Total_100 = models.FloatField (default=0.0, validators=[MinValueValidator (0.0), MaxValueValidator (100.0)])
    class Meta:
        db_table = "vote_votingmodel"
        managed = False
    def __str__(self):
        return self.username

