# Generated by Django 3.2.4 on 2021-08-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'vote_votingmodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Election_Committe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'election_committe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('user_fname', models.CharField(max_length=50)),
                ('user_lname', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=7)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_phone', models.CharField(max_length=20)),
                ('user_role', models.CharField(max_length=30)),
                ('user_status', models.BooleanField(default=True)),
                ('registered', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('key', models.CharField(blank=True, default='000000', max_length=30)),
                ('user_fp', models.CharField(blank=True, default='000000', max_length=30)),
            ],
            options={
                'db_table': 'user_information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'vote_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
