# Generated by Django 3.2.4 on 2021-08-02 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_by', models.CharField(max_length=20)),
                ('camp_title', models.CharField(max_length=200)),
                ('camp_dis', models.TextField(max_length=3000)),
                ('camp_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'campaign_campaign',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VotingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('certifcate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('Total_40', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(40.0)])),
                ('Total_100', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
            options={
                'db_table': 'vote_votingmodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='campaign_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('video_dis', models.TextField(max_length=1000)),
                ('video_file', models.FileField(upload_to='campaign_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='evaluation_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('video_dis', models.TextField(max_length=1000)),
                ('video_file', models.FileField(upload_to='evaluation_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'M4P'])])),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='fileUploading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('file_dis', models.TextField(blank=True, max_length=1000)),
                ('certificate_file', models.FileField(upload_to='certificate', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
    ]